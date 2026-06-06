# syntax=docker/dockerfile:1

# 1. Build stage: Install packages
FROM dhi.io/python:3.13-alpine3.23-dev AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy

RUN pip install --quiet --root-user-action=ignore uv
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# 2. Development stage (Matches your compose target)
FROM builder AS development

ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app
COPY . .

EXPOSE 8000
CMD ["python", "HealthHub/manage.py", "runserver", "0.0.0.0:8000"]

# 3. Production stage (Minimal runtime)
FROM dhi.io/python:3.13-alpine3.23 AS production

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 8000
CMD ["gunicorn", "HealthHub.wsgi:application", "--bind", "0.0.0.0:8000", "--chdir", "HealthHub"]
