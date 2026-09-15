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

partial def anatomy (env : Environment) (pending : List Name)
    (seen : Std.HashSet Name) (frontier : Std.HashSet Name)
    (edges : Std.HashSet (Name × Name)) :
    Std.HashSet Name × Std.HashSet Name × Std.HashSet (Name × Name) :=
  match pending with
  | [] => (seen, frontier, edges)
  | n :: rest =>
    if seen.contains n then anatomy env rest seen frontier edges
    else if !localName n then anatomy env rest seen (frontier.insert n) edges
    else
      match env.find? n with
      | none => anatomy env rest (seen.insert n) frontier edges
      | some info =>
        let refs := refsOf info
        let localRefs := refs.toList.filter localName
        let externalRefs := refs.toList.filter fun x => !localName x
        let newEdges := externalRefs.foldl (fun s x => s.insert (n, x)) edges
        anatomy env (localRefs ++ rest) (seen.insert n)
          (externalRefs.foldl (fun s x => s.insert x) frontier) newEdges

elab "#frontier_anatomy " name:ident : command => do
  let env ← getEnv
  let target := name.getId
  let (localCone, frontier, edges) := anatomy env [target] ∅ ∅ ∅
  logInfo m!"TARGET {target}"
  logInfo m!"LOCAL_COUNT {toString localCone.toList.length}"
  logInfo m!"FRONTIER_COUNT {toString frontier.toList.length}"
  logInfo m!"EDGE_COUNT {toString edges.toList.length}"
  localCone.toList.forM fun d => logInfo m!"LOCAL {d}"
  frontier.toList.forM fun d => logInfo m!"FRONTIER {d}"
  edges.toList.forM fun e => logInfo m!"EDGE {e.1} -> {e.2}"

#frontier_anatomy NavierStokesR3.coreBreakdownStatement
