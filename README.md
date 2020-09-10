# languages_repos
Lists the languages used by the 100 trending public repos on GitHub.



README


This is a  coding chalenge, on how to build a REST API with Django & Python to List the languages used by the 100 trending public repos on GitHub .

Content of the project : 

The project consists of :
languages_repos/
repos/controller_api.py
repos/views.
repos/urls.py
repos/tests.py
languages_repos/urls.py


Installation:

Clone the repository :
 https://github.com/taoufik51/languages_repos.git

Django 3.1
Python 3.7 
django-rest-framework  0.1.0 
djangorestframework    3.11.1
pytz   2020.1
requests  2.24.0

Initial Setup

# activate it 
# mac: `source bin/activate`
# windows: `.\Scripts\activate.bat


in windows :

pip install Django
python  -m venv project-name
project-name\Scripts\activate.bat
pip  install virtualenv
pip  list

django-admin startproject



Update your settings:



INSTALLED_APPS = [
    ...
    'rest_framework',
    'api_repos.apps.ApiConfig',
]
`

Run

python manage.py runserver


Test

python manage.py  test api_repos.tests

