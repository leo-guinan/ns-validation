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

def refsOf (info : ConstantInfo) : Std.HashSet Name :=
  let refs := collectConsts info.type ∅
  match info with
  | .thmInfo v => collectConsts v.value refs
  | .opaqueInfo v => collectConsts v.value refs
  | .defnInfo v => collectConsts v.value refs
  | _ => refs

elab "#refs " name:ident : command => do
  let env ← getEnv
  let n := name.getId
  match env.find? n with
  | none => logError m!"MISSING {n}"
  | some info =>
    let refs := refsOf info
    logInfo m!"DECL {n}"
    logInfo m!"REF_COUNT {refs.toList.length}"
    refs.toList.forM fun r => logInfo m!"REF {r}"

#refs NavierStokesR3.ProblemStatement.breakdownStatement
#refs NavierStokesR3.theorem_1_1
