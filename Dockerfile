FROM python:3.11-slim
WORKDIR /app
COPY requirements-api.lock pyproject.toml README.md ./
COPY research ./research
RUN pip install --no-cache-dir -r requirements-api.lock && pip install --no-cache-dir --no-deps . && useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "research.api:app", "--host", "0.0.0.0", "--port", "8000"]
