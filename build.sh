#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations  
python manage.py migrate

python manage.py createsuperuser --no-input --username=admin3--email=gpra@gmail.com

echo "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin3'); user.set_password('MiPa.contra1!'); user.save()" | python manage.py shell