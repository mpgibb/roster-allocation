# Resource allocation under uncertainty

**Status: research starter, version 0.1.0.** This is an independent portfolio demonstration prepared for Michael P. Gibb, Ph.D. It is not a completed empirical study or a production deployment.

## Executive summary
Exact small-instance allocation with a mean-variance objective.

The current code establishes a transparent baseline. No measured client outcome, financial return, forecasting accuracy, or causal effect is claimed.

## Implemented
- Exact small-instance allocation with a mean-variance objective.
- Explicit input validation and deterministic correctness tests.
- Local FastAPI scaffold with `/health`, `/v1/baseline`, and generated `/docs`.
- A continuous-integration workflow, ready for a Git host.

## Not implemented
Calibrated player forecasts; real data; covariance; optimizer scaling; temporal decision evaluation.

## Data provenance
Only invented inputs are used in tests. No client records or third-party datasets are included. See `DATA.md` before adding data.

## Setup and verification
From this repository directory, Python 3.11 or later:

```bash
python -m unittest discover -s tests -p test_core.py -v
```

For the optional API and its tests:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-api.lock
python -m pip install -e '.[api]'
python -m unittest discover -s tests -v
uvicorn research.api:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` locally. API schemas describe request fields. No endpoint is currently deployed by this package. On Windows, activate with `.venv\Scripts\activate`.

## Evaluation and limitations
Independent contributions; consistent cost/performance units. A variance penalty is a preference, not an estimated business utility.

Correctness tests verify arithmetic and specified behavior; they do not validate an empirical model. Follow `RESEARCH_PLAN.md` before interpreting results. Future reports must retain data version, code commit, configuration, baseline, evaluation window, sample size, and limitations.

## Architecture
`research/core.py` contains the baseline. `research/api.py` validates requests and calls it. Tests are independent of the website. Training, persisted artifacts, and external data ingestion remain future work.

## Source and reproducible environment
Canonical repository: https://github.com/mpgibb/roster-allocation

Imported from `Michael_Gibb_Research_Starters.zip` on 2026-09-28. The archive contained no Git internals; the first commit preserves the provided starter. Archive SHA-256: `2195ca960288b3fc54d0920c782a1645fdd7b9a03f371f2ecd6ed27aa926eee2`.

Each starter uses its own `research` package. Keep separate virtual environments; do not install the four packages into one environment.

For a fully locked Python 3.11 environment, use uv 0.12.19:

```bash
uv sync --frozen --extra api --python 3.11
uv run --frozen --extra api python -m unittest discover -s tests -v
uv run --frozen --extra api uvicorn research.api:app --host 127.0.0.1 --port 8000
```

`requirements-api.lock` is retained from the supplied archive. `uv.lock` is the canonical complete resolution for development and CI. When changing dependencies, update the lock and rerun the tests. The standard pip instructions above remain available.

## Authorship and review
Initial scaffold and baseline code generated with Codex assistance from a design discussion with Gemini. Michael's technical review and project-specific research are still required before this represents completed portfolio work.

## License
No open-source license has been granted. Source is published for inspection; public availability does not grant reuse rights. Michael may choose a license later. Dataset rights must be assessed separately.
