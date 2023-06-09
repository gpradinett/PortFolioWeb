#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --no-input --username=admin --email=gpra@gmail.com

expect << EOF
spawn python manage.py changepassword admin
expect "Password:"
send "MiPa.contra1!\r"
expect eof
EOF