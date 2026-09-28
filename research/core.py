"""Exact small-instance allocation baseline; synthetic inputs only."""
from dataclasses import dataclass
from itertools import combinations
from math import isfinite
from collections import Counter

@dataclass(frozen=True)
class Candidate:
    id: str
    position: str
    cost: float
    mean: float
    variance: float

def allocate(candidates, budget, requirements, risk_aversion=0.0):
    """Maximize sum(mean) - lambda * sum(variance), assuming independence.

    Enumerates all feasible subsets. Deliberately limited to 20 candidates.
    Ties resolve lexicographically by ID, independent of input ordering.
    Returns None if the constraints are infeasible.
    """
    candidates = list(candidates)
    if len(candidates) > 20:
        raise ValueError("Exact baseline limited to 20 candidates")
    if not isfinite(budget) or budget < 0 or not isfinite(risk_aversion) or risk_aversion < 0:
        raise ValueError("Budget and risk_aversion must be finite and nonnegative")
    if not requirements or any(not isinstance(v,int) or isinstance(v,bool) or v < 0 for v in requirements.values()):
        raise ValueError("Requirements must be nonnegative integer counts")
    if len({c.id for c in candidates}) != len(candidates):
        raise ValueError("Candidate IDs must be unique")
    for c in candidates:
        if not c.id or not c.position or not all(isfinite(x) for x in [c.cost,c.mean,c.variance]) or c.cost < 0 or c.variance < 0:
            raise ValueError("Invalid candidate")
    target = {k:v for k,v in requirements.items() if v}
    best, best_score = None, float('-inf')
    for roster in combinations(sorted(candidates,key=lambda c:c.id), sum(requirements.values())):
        if dict(Counter(c.position for c in roster)) != target or sum(c.cost for c in roster) > budget:
            continue
        score = sum(c.mean-risk_aversion*c.variance for c in roster)
        if score > best_score:
            best,best_score = roster,score
    if best is None:
        return None
    return {"ids":[c.id for c in best],"cost":sum(c.cost for c in best),"expected_performance":sum(c.mean for c in best),"variance":sum(c.variance for c in best),"objective":best_score,"assumption":"independent candidate outcomes"}
