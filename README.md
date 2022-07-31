Abertura do projeto

python –m venv venv (criar ambiente virtual)

pip install django (instalar Django)

django-admin startproject ars .

settings (Alterar idioma e horário)

LANGUAGE_CODE: 'pt-br'

TIME_ZONE: 'America/Sao_Paulo'

python manage.py runserver (rodar)

pip freeze > requirements.txt (criar requirements.txt)

pip install –r requirements.txt (instalar requirements.txt)


CORE

python manage.py startapp core (criar app)

settings (registrar app)

core/templates/home.html

settings/TEMPLATES/DIRS: [os.path.join(BASE_DIR, 'templates')]

core/views: home

core/urls: home

ars/urls: core

core/templates: base.html, header.html e messages.html

AUTHENTICATION

python manage.py startapp authentication (criar app) - OK

settings (registrar app) - OK

authentication/models: CustomUserManager e CustomUser - OK

ars/settings: AUTH_USER_MODEL = "authentication.CustomUser" - OK

authentication/admin: UserAdmin - OK



authentication/templates/registration: register.html - OK

authentication/urls: register - OK

ars/urls: authentication - OK

authentication/views: register: (aula 22 - OK, falta send email)

Se erro "no such table": python manage.py migrate --run-syncdb

Teste: nteste, steste, bgh@bgh.kinghost.net, 123456