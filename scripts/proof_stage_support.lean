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
    (seen : Std.HashSet Name) (frontier : Std.HashSet Name) :
    Std.HashSet Name × Std.HashSet Name :=
  match pending with
  | [] => (seen, frontier)
  | n :: rest =>
    if seen.contains n then cone env rest seen frontier
    else if !localName n then cone env rest seen (frontier.insert n)
    else match env.find? n with
      | none => cone env rest (seen.insert n) frontier
      | some info =>
        let refs := refsOf info
        let locals := refs.toList.filter localName
        let externals := refs.toList.filter fun x => !localName x
        cone env (locals ++ rest) (seen.insert n)
          (externals.foldl (fun s x => s.insert x) frontier)

elab "#stage_support " name:ident : command => do
  let env ← getEnv
  let target := name.getId
  let (locals, frontier) := cone env [target] ∅ ∅
  logInfo m!"ANCHOR {target}"
  logInfo m!"LOCAL_COUNT {locals.toList.length}"
  logInfo m!"FRONTIER_COUNT {frontier.toList.length}"
  locals.toList.forM fun n => logInfo m!"LOCAL {n}"
  frontier.toList.forM fun n => logInfo m!"FRONTIER {n}"

#stage_support NavierStokesR3.theorem_1_1_with_initial_rest
#stage_support NavierStokesR3.theorem_1_1
