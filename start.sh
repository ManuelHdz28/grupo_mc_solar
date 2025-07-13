#!/usr/bin/env bash
python backend/manage.py migrate
gunicorn backend.config.wsgi