#!/bin/bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn jango_deployee.wsgi:application --bind 0.0.0.0:$PORT