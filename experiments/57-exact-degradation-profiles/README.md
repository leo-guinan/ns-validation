# Experiment 57 — exact adversarial and feasible degradation profiles

Two quantifiers are kept separate:

```text
W_adv(r):  worst-case minimum width over |D|≤r, with infeasibility = infinity
W_feas(r): widest minimum width among feasible exact-|D|=r deletions
```

The actual adversarial staircases below incorporate every finite width threshold before collapse:

```text
component 8:  3,3,3,3,infinity       for budgets 0..4
component 11: 3 through budget 15, 4 at budgets 16..20, infinity at 21
component 12: 1 at budget 0, 2 at budget 1, infinity at 2
component 21: 2 at budget 0, 3 at budgets 1..3, infinity at 4
component 45: 1 at budget 0, 2 at budget 1, infinity at 2
```

The literal receipt establishes components 12 and 45 at current width 1; component 21 is the current-width-2 case.

Feasible transition witnesses remain separate:

```text
component 8:  width 3→4 at 4 deletions
component 11: width 3→4 at 16 deletions
component 12: width 1→2 at 1 deletion
component 21: width 2→3 at 1 deletion; width 3→4 at 4 deletions
component 45: width 1→2 at 1 deletion
```

Components 8 and 21 each have the same-budget split: at four deletions, one deletion set leaves a feasible wider cover while another makes the component infeasible. Therefore those observations cannot be represented as a single feasible/adversarial transition curve.

Pure substitution components have `W_adv(r)=1` below their candidate count and `W_adv(r)=infinity` at or above it.

These are adversarial combinatorial thresholds, not failure probabilities or operational reliability claims.
