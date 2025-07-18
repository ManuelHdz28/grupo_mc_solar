#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# Crear superusuario solo si no existe
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
username = '$DJANGO_SUPERUSER_USERNAME'; \
email = '$DJANGO_SUPERUSER_EMAIL'; \
password = '$DJANGO_SUPERUSER_PASSWORD'; \
\
User.objects.filter(username=username).exists() or \
User.objects.create_superuser(username=username, email=email, password=password)" \
| python manage.py shell


