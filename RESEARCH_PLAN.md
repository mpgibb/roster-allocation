# Research plan

## Implemented baseline
Exact small-instance allocation with a mean-variance objective.

## Next work
Calibrated player forecasts; real data; covariance; optimizer scaling; temporal decision evaluation.

## Evaluation contract
1. Define the decision and estimand before selecting an advanced model.
2. Freeze source data and explicit temporal boundaries when applicable.
3. Establish strong, simple baselines and meaningful failure cases.
4. Keep model/strategy selection separate from final evaluation.
5. Report uncertainty, sample sizes, exclusions, and comparison methods.
6. Record limits: Independent contributions; consistent cost/performance units. A variance penalty is a preference, not an estimated business utility.
7. Publish machine-readable metrics only after reproducible evaluation.

## Intended production work
Version model and data artifacts; validate requests; measure latency and reliability; add monitoring based on actual failure modes; configure deployment controls for the selected host. The current scaffold is local and makes no production-readiness claim.
