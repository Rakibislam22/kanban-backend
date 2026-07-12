#!/usr/bin/env bash
# This script is run by the hosting provider to build and deploy the application.

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
# The migrate command must run after installing dependencies to apply database schema changes.
python manage.py migrate