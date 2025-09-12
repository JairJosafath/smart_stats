FROM python:slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG service
ENV SERVICE=${service}

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN uv venv && . .venv/bin/activate \
    && uv pip install -r pyproject.toml  \
    && uv sync

COPY services/$SERVICE services/$SERVICE

COPY apps/$SERVICE/app.py /app/app.py

COPY services/__init__.py services/__init__.py

EXPOSE 8000

CMD [ "uv", "run", "app.py" ]