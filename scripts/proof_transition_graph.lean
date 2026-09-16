import Lean
import NavierStokes.R3.Theorem
open Lean Elab Command

partial def collectConsts (e : Expr) (out : Std.HashSet Name) : Std.HashSet Name :=
  match e with
  | .const n _ => out.insert n
  | .app f a => collectConsts a (collectConsts f out)
  | .lam _ t b _ => collectConsts b (collectConsts t out)
  | .forallE _ t b _ => collectConsts b (collectConsts t out)
  | .letE _ t v b _ => collectConsts b (collectConsts v (collectConsts t out))
  | .mdata _ x => collectConsts x out
  | .proj _ _ x => collectConsts x out
  | _ => out

def localName (n : Name) : Bool := n.toString.startsWith "NavierStokesR3"
def refsOf (info : ConstantInfo) : Std.HashSet Name :=
  let refs := collectConsts info.type ∅
  match info with
  | .thmInfo v => collectConsts v.value refs
  | .opaqueInfo v => collectConsts v.value refs
  | .defnInfo v => collectConsts v.value refs
  | _ => refs

partial def cone (env : Environment) (pending : List Name)
    (seen : Std.HashSet Name) (frontier : Std.HashSet Name)
    (edges : Std.HashSet (Name × Name)) :
    Std.HashSet Name × Std.HashSet Name × Std.HashSet (Name × Name) :=
  match pending with
  | [] => (seen, frontier, edges)
  | n :: rest =>
    if seen.contains n then cone env rest seen frontier edges
    else if !localName n then cone env rest seen (frontier.insert n) edges
    else match env.find? n with
      | none => cone env rest (seen.insert n) frontier edges
      | some info =>
        let refs := refsOf info
        let locals := refs.toList.filter localName
        let externals := refs.toList.filter fun x => !localName x
        let newEdges := locals.foldl (fun s x => s.insert (n, x)) edges
        cone env (locals ++ rest) (seen.insert n)
          (externals.foldl (fun s x => s.insert x) frontier) newEdges

elab "#transition " name:ident : command => do
  let env ← getEnv
  let target := name.getId
  match env.find? target with
  | none => logError m!"MISSING {target}"
  | some info =>
    let direct := refsOf info
    let (locals, frontier, edges) := cone env [target] ∅ ∅ ∅
    logInfo m!"NODE {target}"
    logInfo m!"SUPPORT_LOCAL {locals.toList.length}"
    logInfo m!"SUPPORT_FRONTIER {frontier.toList.length}"
    direct.toList.filter localName |>.forM fun n => logInfo m!"DIRECT_LOCAL {n}"
    edges.toList.forM fun e => logInfo m!"LOCAL_EDGE {e.1} -> {e.2}"
    locals.toList.forM fun n =>
      match env.find? n with
      | some i =>
        (refsOf i).toList.filter (fun x => !localName x) |>.forM fun x => logInfo m!"EXTERNAL_EDGE {n} -> {x}"
      | none => pure ()
    locals.toList.forM fun n => logInfo m!"LOCAL {n}"
    frontier.toList.forM fun n => logInfo m!"FRONTIER {n}"

#transition NavierStokesR3.theorem_1_1_with_initial_rest
#transition NavierStokesR3.theorem_1_1
#transition NavierStokesR3.candidateStatement
#transition NavierStokesR3.coreBreakdownStatement
#transition NavierStokesR3.ProblemStatement.breakdownStatement
#transition NavierStokesR3.theorem_1_1_with_dissipation
