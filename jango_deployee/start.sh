#I\bin\bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# gunicorn yourprject_filename.wsgi:application --bind 0.0.0.$PORT
gunicorn jango_deployee.wsgi:application --bind 0.0.0.$PORT
