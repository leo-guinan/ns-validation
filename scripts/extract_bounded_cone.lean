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

partial def boundedCone (env : Environment) (pending : List (Name × Nat))
    (seen : Std.HashSet Name) (frontier : Std.HashSet Name) (maxDepth : Nat) :
    Std.HashSet Name × Std.HashSet Name × Nat :=
  match pending with
  | [] => (seen, frontier, maxDepth)
  | (n, depth) :: rest =>
    if seen.contains n then boundedCone env rest seen frontier maxDepth
    else if !localName n then boundedCone env rest seen (frontier.insert n) maxDepth
    else
      match env.find? n with
      | none => boundedCone env rest (seen.insert n) frontier maxDepth
      | some info =>
        let refs := refsOf info
        let localRefs := refs.toList.filter localName
        let externalRefs := refs.toList.filter fun x => !localName x
        let next := localRefs.map fun x => (x, depth + 1)
        boundedCone env (next ++ rest) (seen.insert n)
          (externalRefs.foldl (fun s x => s.insert x) frontier) (max maxDepth depth)

elab "#bounded_deps " name:ident : command => do
  let env ← getEnv
  let n := name.getId
  match env.find? n with
  | none => logError m!"declaration not found: {n}"
  | some info =>
    let direct := refsOf info
    let (localCone, frontier, depth) := boundedCone env [(n, 0)] ∅ ∅ 0
    logInfo m!"TARGET {n}"
    logInfo m!"DIRECT_COUNT {toString direct.toList.length}"
    logInfo m!"LOCAL_CONE_COUNT {toString localCone.toList.length}"
    logInfo m!"FRONTIER_COUNT {toString frontier.toList.length}"
    logInfo m!"MAX_LOCAL_DEPTH {toString depth}"
    direct.toList.forM fun d => logInfo m!"DIRECT {d}"
    localCone.toList.forM fun d => logInfo m!"LOCAL {d}"
    frontier.toList.forM fun d => logInfo m!"FRONTIER {d}"

#bounded_deps NavierStokesR3.coreBreakdownStatement
