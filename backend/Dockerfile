FROM python:3.12-alpine AS builder

WORKDIR /backend
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.in-project true

COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes -o requirements.txt

FROM python:3.12-alpine

RUN apk add build-base vips vips-tools vips-dev

WORKDIR /backend
ENV PYTHONUNBUFFERED=1

COPY --from=builder /backend/requirements.txt .
RUN python -m pip install pip==24.0.0
RUN pip install -r requirements.txt

COPY ./src/ .

CMD python manage.py migrate \
 && python manage.py collectstatic --noinput \
 && python manage.py createadmin \
 && gunicorn config.wsgi:application --bind 0.0.0.0:$BACKEND_PORT
