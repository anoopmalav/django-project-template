{{ project_name|title }}
{% with project_name_length=project_name|length %}{{"=================================================="|truncatechars:project_name_length|slice:":-3" }}==={% endwith %}

# Important Notes

This guide is long because it covers many cases and includes all commands you need.

This installation guide was created for and tested on **Ubuntu 14.04** operating systems.

This is the official installation guide to set up a production server. To set up a **development installation** and to contribute read `Contributing.md`.

The following steps have been known to work. Please **use caution when you deviate** from this guide. Make sure you don't violate any assumptions {{project_name|title}} makes about its environment.

# Overview

The  {{project_name|title}} installation consists of setting up the following components:

1. Packages / Dependencies
1. System Users
1. Database
1. {{project_name|title}}
1. Supervisor
1. Nginx
1. Update Existing Setup to Newer Version

## Packages / Dependencies

Run following commands

    sudo apt-get update
    sudo apt-get -y upgrade

**Note:** During this installation some files will need to be edited manually. If you are familiar with vim set it as default editor with the commands below. If you are not familiar with vim please skip this and keep using the default editor.

    # Install vim and set as default editor
    sudo apt-get install -y vim-gnome
    sudo update-alternatives --set editor /usr/bin/vim.gnome

Install the required packages (needed to compile Ruby and native extensions to Ruby gems):

    sudo apt-get install -y build-essential git-core libssl-dev libffi-dev curl redis-server checkinstall libcurl4-openssl-dev python-docutils pkg-config python3-dev python-dev python-virtualenv

**Note:** In order to receive mail notifications, make sure to install a mail server. The recommended mail server is postfix and you can install it with:

    sudo apt-get install -y postfix

Then select 'Internet Site' and press enter to confirm the hostname.

# System Users

Create a `{{ project_name }}` user for {{ project_name|title }}:

    sudo adduser --disabled-login --gecos '{{ project_name|title }}' {{ project_name }}

# Database

We recommend using a PostgreSQL database.

    # Install the database packages
    sudo apt-get install -y postgresql postgresql-client libpq-dev

    # Login to PostgreSQL
    sudo -u postgres psql -d postgres

    # Create a user for {{ project_name|title }}
    # Do not type the 'postgres=#', this is part of the prompt
    postgres=# CREATE USER {{ project_name }} WITH PASSWORD '123456' CREATEDB;

    # Create the {{ project_name|title }} production database & grant all privileges on database
    postgres=# CREATE DATABASE {{ project_name }}_production OWNER {{ project_name }};

    # Quit the database session
    postgres=# \q

    # Try connecting to the new database with the new user
    sudo -u {{ project_name }} -H psql -d {{ project_name }}_production

    # Quit the database session
    {{ project_name }}_production> \q

# {{ project_name|title }}

    # We'll install {{ project_name|title }} into home directory of the user "{{ project_name }}"
    cd /home/{{ project_name }}

## Clone the Source

    # Clone {{ project_name|title }} repository
    sudo -u {{ project_name }} -H {{ project_name }} clone https://github.com/{{ project_name }}/{{ project_name }}.git {{ project_name }}

## Configure It

    # Switch User {{ project_name }}
    sudo su {{ project_name }}

    # Go to {{ project_name|title }} installation folder
    cd /home/{{ project_name }}/{{ project_name }}

    # Virtual Envirnoment and requirements
    virtualenv -p /usr/bin/python3.4 env
    source env/bin/activate
    pip install -r requirements.txt

## Project and Database Configuartion Settings

    # Edit desired configurations in config/local.py i.e. STATICFILES_DIRS
    cp config/local.py.example config/local.py
    chmod o-rwx config/local.py
    editor config/local.py

Example:

        DEBUG = False

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': '{{ project_name }}_production',
                'USER': '{{ project_name }}',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '',
            }
        }

## Validate configurations

    ./manage.py validate

## Migrate Database & Seed Default Data

    ./manage.py migrate
    ./manage.py loaddata fixtures/default.json

## Load Assets

    ./manage.py collectstatic

## Gunicorn Or uWSGI

    # Copy either of the configuration file for respective server
    cp scripts/gunicorn.bash scripts/runserver.bash

    OR

    cp scripts/uwsgi.bash scripts/runserver.bash

    # Make it executable
    chmod u+x scripts/runserver.bash

## Celery & Celerybeat

    cp scripts/celery.bash.example scripts/celery.bash
    cp scripts/celerybeat.bash.example scripts/celerybeat.bash

## Exit User {{ project_name }}

    exit

# Supervisor

## Installation

    sudo apt-get install -y supervisor

    # Go to {{ project_name|title }} installation folder
    cd /home/{{ project_name }}/{{ project_name }}

## Configuration

    sudo cp config/supervisor/{{ project_name }}.conf /etc/supervisor/conf.d/{{ project_name }}.conf
    sudo cp config/supervisor/{{ project_name }}_celery.conf /etc/supervisor/conf.d/{{ project_name }}_celery.conf
    sudo cp config/supervisor/{{ project_name }}_celerybeat.conf /etc/supervisor/conf.d/{{ project_name }}_celerybeat.conf

## Supervisor Configuration Update

    sudo service supervisor restart
    sudo supervisorctl reread
    sudo supervisorctl update

# Nginx

## Installation

    sudo apt-get install -y nginx

## Site Configuration

    # Copy the example site config:
    sudo cp config/nginx/{{ project_name }} /etc/nginx/sites-available/{{ project_name }}
    sudo ln -s /etc/nginx/sites-available/{{ project_name }} /etc/nginx/sites-enabled/{{ project_name }}

Make sure to edit the config file to match your setup:

    # Change YOUR_SERVER_FQDN to the fully-qualified
    # domain name of your host serving {{ project_name|title }}.
    sudo editor /etc/nginx/sites-available/{{ project_name }}

**Note:** If you want to use HTTPS, replace the `{{ project_name }}` Nginx config with `{{ project_name }}-ssl`. See [Using HTTPS](#using-https) for HTTPS configuration details.

## Test Configuration

Validate your `{{ project_name }}` or `{{ project_name }}-ssl` Nginx config file with the following command:

    sudo nginx -t

You should receive `syntax is okay` and `test is successful` messages. If you receive errors check your `{{ project_name }}` or `{{ project_name }}-ssl` Nginx config file for typos, etc. as indicated in the error message given.

## Provide access to static files and error templates

    sudo adduser nginx {{ project_name }}
    sudo chmod -R 750 /home/{{ project_name }}/{{ project_name }}/static/
    sudo chmod -R 750 /home/{{ project_name }}/{{ project_name }}/templates/

## Restart

    sudo service nginx restart

# Update Existing Setup to Newer Version


# Using HTTPS

To use {{ project_name|title }} with HTTPS:


Using a self-signed certificate is discouraged but if you must use it follow the normal directions then:

1. Generate a self-signed SSL certificate:

    ```
    mkdir -p /etc/nginx/ssl/
    cd /etc/nginx/ssl/
    sudo openssl req -newkey rsa:2048 -x509 -nodes -days 3560 -out {{ project_name }}.crt -keyout {{ project_name }}.key
    sudo chmod o-r {{ project_name }}.key
    ```
