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

def projectName (n : Name) : Bool := n.toString.startsWith "NavierStokesR3"

def allowed (mode : Nat) (target n : Name) (depth : Nat) : Bool :=
  match mode with
  | 0 => n == target
  | 1 => projectName n && depth <= 1
  | 2 => projectName n
  | _ => false

def refsOf (info : ConstantInfo) : Std.HashSet Name :=
  let refs := collectConsts info.type ∅
  match info with
  | .thmInfo v => collectConsts v.value refs
  | .opaqueInfo v => collectConsts v.value refs
  | .defnInfo v => collectConsts v.value refs
  | _ => refs

partial def sweepCone (env : Environment) (mode : Nat) (target : Name)
    (pending : List (Name × Nat)) (seen : Std.HashSet Name)
    (frontier : Std.HashSet Name) (maxDepth : Nat) :
    Std.HashSet Name × Std.HashSet Name × Nat :=
  match pending with
  | [] => (seen, frontier, maxDepth)
  | (n, depth) :: rest =>
    if seen.contains n then sweepCone env mode target rest seen frontier maxDepth
    else if !allowed mode target n depth then
      sweepCone env mode target rest seen (frontier.insert n) maxDepth
    else
      match env.find? n with
      | none => sweepCone env mode target rest (seen.insert n) frontier maxDepth
      | some info =>
        let refs := refsOf info
        let next := refs.toList.map fun x => (x, depth + 1)
        sweepCone env mode target (next ++ rest) (seen.insert n) frontier (max maxDepth depth)

elab "#boundary_sweep " name:ident : command => do
  let env ← getEnv
  let target := name.getId
  let direct := match env.find? target with
    | some info => refsOf info
    | none => ∅
  for mode in [0, 1, 2] do
    let (localCone, frontier, depth) := sweepCone env mode target [(target, 0)] ∅ ∅ 0
    logInfo m!"BOUNDARY {toString mode} DIRECT {toString direct.toList.length} LOCAL {toString localCone.toList.length} FRONTIER {toString frontier.toList.length} DEPTH {toString depth}"

#boundary_sweep NavierStokesR3.coreBreakdownStatement
