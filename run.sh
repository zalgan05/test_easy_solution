#!/bin/sh
echo "Running migrations..."
python manage.py makemigrations;
python manage.py migrate;

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

echo "Starting Gunicorn..."
gunicorn --bind 0:8000 easy_solution.wsgi;