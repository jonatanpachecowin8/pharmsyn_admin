virtualenv -p /usr/bin/python3.10 venv

source venv/bin/activate

pip install django

pip install --upgrade pip

Initalize project 
django-admin startproject pharmsyn

pip freeze > requirements.txt

python manage.py migrate