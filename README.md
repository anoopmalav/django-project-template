{% if False %}
# Django 1.8 Project Template

## About

This template is based off of the work of [UPVGO](http://upvgo.com/) and emend, as well as experience with other Django layouts/project templates.

This project template is designed for Django 1.4's new startproject template option. This version of the project template is designed for Django 1.8.

As much as I could, all the code has been updated to use the new suggested layout
and functionality in Django 1.8.

## Features

By default, this project template includes:

A set of basic templates built from HTML5Boilerplate 4.1.0 and Twitter Bootstrap 3.2.0 (located in the
base app, with css and javascript loaded from CloudFlare CDN by default).

Templating:

- django_compressor for compressing javascript/css/less/sass

Security:

- bleach
- bcrypt - uses bcrypt for password hashing by default

Background Tasks:

- Celery

Migrations:

- Django built-in migrations

Caching:

- python-memcached

Admin:

- Includes django-debug-toolbar for development and production (enabled for superusers)

Testing:

- nose and django-nose
- pylint, pep8, and coverage

Any of these options can be added, modified, or removed as you like after creating your project.

## How to use this project template to create your project

- Create your working directory ($ mkdir ~/Work; cd ~/Work)
- Install Django 1.8 ($ sudo apt-get install python-django )
- $ django-admin startproject --template http://gitlab.finoit.com/python/django-project-template/repository/archive.zip --extension py,md,rst,html,js,conf,example,bash --name CHANGELOG,project_name,project_name-ssl projectname
- $ cd projectname
- Create virtual environment and activate.
- $ virtualenv -p /usr/bin/python3.4 env
- $ source env/bin/activate
- Uncomment your preferred requirements
- $ pip install -r requirements.txt
- $ cp projectname/config/local.py.example projectname/config/local.py
- Update fields in the models of apps available in projectname/libs/
- $ python manage.py makemigrations
- $ python manage.py migrate
- $ python manage.py runserver

That's all you need to do to get the project ready for development. When you deploy your project into production, you should look into getting certain settings from environment variables or other external sources. (See SECRET_KEY for an example.)

There isn't a need to add config/local.py to your source control, but there are multiple schools of thought on this. The method I use here is an example where each developer has their own config/local.py with machine-specific settings. You will also need to create a version of config/local.py for use in production that you will put into place with your deployment system.

The second school of thought is that all settings should be versioned, so that as much of the code/settings as possible is the same across all developers and test/production servers. If you prefer this method, then make sure *all* necessary settings are properly set in config/settings.py.

{% endif %}
{{ project_name|title }}
{% with project_name_length=project_name|length %}{{"=================================================="|truncatechars:project_name_length|slice:":-3" }}==={% endwith %}

## About

Describe your project here.

## Prerequisites

- Linux (Preferably Ubuntu)
- Python 3.4+
- pip
- virtualenv

## Installation

See Install.md

## Contributing

See Contributing.md

## License

All the rights are reserved to Finoit Technologies Pvt. Ltd. Noida

As a developer you can modify content of the project. But you are required not to use any of the component in any other project without permission from company.
