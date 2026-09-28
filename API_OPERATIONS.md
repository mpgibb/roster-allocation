# Local API scaffold

No endpoint is deployed. The website has no live inference dependency.

- Start with `uv run --frozen --extra api uvicorn research.api:app --host 127.0.0.1 --port 8000`.
- `/health` reports implementation and version; `/docs` exposes the request schema.
- `/v1/baseline` returns version 0.1.0 and research-baseline status. Responses are computed from user-supplied inputs, not trained model inference.
- Pydantic rejects undeclared fields and invalid inputs with HTTP 422; core domain errors are mapped to HTTP 422 where applicable.
- No authentication, rate limiting, durable storage, trained artifacts or operational monitoring exists. Do not expose the scaffold unchanged as a production service.
- Roster search is capped at 20 candidates. Other baselines are scalar calculations.
- Before a useful Render deployment: define resource/body/time limits, request logging without sensitive payloads, dependency/image pinning, health checks, abuse controls, and error/overflow behavior; bind to `0.0.0.0` and Render's `PORT`.
- A Dockerfile is supplied for local evaluation; its Python minor-version image tag is not a pinned production image digest.

A service should be deployed only when a specific website interaction needs it and its scientific and operational behavior has been evaluated.
