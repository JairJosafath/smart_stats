FROM python:slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG service
ENV SERVICE="services/${service}"

WORKDIR $SERVICE

COPY pyproject.toml .
COPY uv.lock .

RUN uv venv && . .venv/bin/activate \
    && uv pip install -r pyproject.toml  \
    && uv sync

COPY $SERVICE .

CMD [ "uv", "run", "app.py" ]