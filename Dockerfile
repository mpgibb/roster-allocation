FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY research ./research
RUN pip install --no-cache-dir '.[api]' && useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "research.api:app", "--host", "0.0.0.0", "--port", "8000"]
