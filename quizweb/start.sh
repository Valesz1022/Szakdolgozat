#!/bin/bash
set -o errexit

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn quizweb.wsgi:application --bind 0.0.0.0:$PORT
