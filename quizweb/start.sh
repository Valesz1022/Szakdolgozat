#!/bin/bash

# Migrate database
python manage.py migrate

# Collect static files (ha vannak)
python manage.py collectstatic --noinput

# Indítsd a Django-t
python manage.py runserver 0.0.0.0:$PORT
