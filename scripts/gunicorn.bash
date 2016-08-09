#!/bin/bash

# Name of the application
NAME="{{ project_name }}"

# Django project directory
DJANGODIR=/home/{{ project_name }}/{{ project_name }}

# The user to run as
USER={{ project_name }}

# The group to run as
GROUP={{ project_name }}

# How many worker processes should Gunicorn spawn
NUM_WORKERS=8

# Which settings file should Django use
DJANGO_SETTINGS_MODULE=config.settings

# WSGI module name
DJANGO_WSGI_MODULE=config.wsgi

# Access logs
ACCESS_LOG='/home/{{ project_name }}/{{ project_name }}/tmp/logs/access.log'

# Error logs
ERROR_LOG='/home/{{ project_name }}/{{ project_name }}/tmp/logs/error.log'

# Log Level
LOG_LEVEL=debug # Options are debug, info, warning, error, critical

# Socket File to bind to
SOCKFILE=/home/{{ project_name }}/{{ project_name }}/tmp/sockets/gunicorn.sock

################################# END OF CONFIGURATIONS #################################


# ---------------------------------------------------------------------------------------

# Change to project directory
cd $DJANGODIR

# Activate the virtual environment
source env/bin/activate

# Activate project environment
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn $DJANGO_WSGI_MODULE:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=$LOG_LEVEL \
  --bind=unix:$SOCKFILE \
  --access-logfile $ACCESS_LOG \
  --error-logfile $ERROR_LOG
