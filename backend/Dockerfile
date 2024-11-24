FROM python:3.12-alpine AS builder

WORKDIR /backend
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.in-project true

COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes -o requirements.txt

FROM python:3.12

RUN apt update -y
RUN apt install -y --no-install-recommends build-essential libvips-dev

WORKDIR /backend
ENV PYTHONUNBUFFERED=1

COPY --from=builder /backend/requirements.txt .
RUN pip install -r requirements.txt

COPY ./src/ .

CMD python manage.py migrate \
 && python manage.py collectstatic --noinput \
 && python manage.py createadmin \
 && gunicorn config.wsgi:application --bind 0.0.0.0:$BACKEND_PORT
