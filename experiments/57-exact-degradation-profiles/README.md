# Experiment 57 — exact adversarial and feasible degradation profiles

Two quantifiers are kept separate:

```text
W_adv(r):  worst-case minimum width over |D|≤r, with infeasibility = infinity
W_feas(r): widest minimum width among feasible exact-|D|=r deletions
```

The listed finite transitions are feasible-width witnesses. The adversarial profile becomes infinity as soon as any infeasible deletion set exists.

Kernel adversarial landmarks:

```text
component 8:  W_adv=3 below r=4; W_adv=infinity from r=4
component 11: W_adv=3 below r=21; W_adv=infinity from r=21
component 12: W_adv=2 below r=2; W_adv=infinity from r=2
component 21: W_adv=2 below r=4; W_adv=infinity from r=4
component 45: W_adv=2 below r=2; W_adv=infinity from r=2
```

Feasible transition witnesses:

```text
component 8:  width 3→4 at 4 deletions
component 11: width 3→4 at 16 deletions
component 12: width 2→3 at 1 deletion
component 21: width 2→3 at 1 deletion; width 3→4 at 4 deletions
component 45: width 2→3 at 1 deletion
```

Components 8 and 21 each have the same-budget split: at four deletions, one deletion set leaves a feasible wider cover while another makes the component infeasible. Therefore those observations cannot be represented as a single adversarial width transition.

Pure substitution components have `W_adv(r)=1` below their candidate count and `W_adv(r)=infinity` at or above it.

These are adversarial combinatorial thresholds, not failure probabilities or operational reliability claims.
