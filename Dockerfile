FROM public.ecr.aws/lambda/python:3.12
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG service
ENV SERVICE="services/${service}"

COPY $SERVICE ${LAMBDA_TASK_ROOT}
COPY pyproject.toml ${LAMBDA_TASK_ROOT}
COPY uv.lock ${LAMBDA_TASK_ROOT}

RUN uv pip install -r ${LAMBDA_TASK_ROOT}/pyproject.toml --system

CMD [ "app.py" ]