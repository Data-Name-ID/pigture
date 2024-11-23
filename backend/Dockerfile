FROM python:3.12 AS builder

WORKDIR /backend
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.in-project true

COPY poetry.lock pyproject.toml ./
RUN poetry install --without lint --no-interaction --no-ansi


FROM python:3.12

WORKDIR /backend
ENV PYTHONUNBUFFERED=1
ENV BIN_PATH=/backend/.venv/bin/

COPY --from=builder /backend/.venv/ ./.venv/

COPY ./src/ .

CMD $BIN_PATH/python manage.py migrate && $BIN_PATH/python manage.py collectstatic --noinput && python manage.py createadmin && $BIN_PATH/gunicorn config.wsgi:application --bind 0.0.0.0:$BACKEND_PORT
