#!/bin/bash

# Name of the application
NAME="{{ project_name }}"

# Django project directory
DJANGODIR=/home/{{ project_name }}/{{ project_name }}

# The user to run as
USER={{ project_name }}

# The group to run as
GROUP={{ project_name }}

# How many worker processes should uWSGI spawn
NUM_PROCESSES=8

# Which settings file should Django use
DJANGO_SETTINGS_MODULE=config.settings

# WSGI module name
DJANGO_WSGI_MODULE=config.wsgi

# LOG File
LOG_FILE='/home/{{ project_name }}/{{ project_name }}/tmp/logs/error.log'

# Socket File to bind to
SOCKFILE=/home/{{ project_name }}/{{ project_name }}/tmp/sockets/uwsgi.sock

################################# END OF CONFIGURATIONS #################################


# ---------------------------------------------------------------------------------------

# Change to project directory
cd $DJANGODIR

# Activate the virtual environment
source env/bin/activate

# Activate project environment
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Start your Django uWSGI
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemonize)

exec uwsgi --master --module=$DJANGO_WSGI_MODULE:application \
    --procname=$NAME \
    --socket=unix:$SOCKFILE \
    --processes=$NUM_PROCESSES \                 # number of worker processes
    --uid=$USER --gid=$GROUP \
    --harakiri=20 \                 # respawn processes taking more than 20 seconds
    --max-requests=5000 \           # respawn processes after serving 5000 requests
    --vacuum \                      # clear environment on exit
    --logto=$LOG_FILE
    