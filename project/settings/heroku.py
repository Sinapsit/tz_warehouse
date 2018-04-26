# -*- coding: utf-8 -*-
"""Local settings."""
from .base import *
import django_heroku

DEBUG = True

ALLOWED_HOSTS = ['*']


# Activate Django-Heroku.
django_heroku.settings(locals())
