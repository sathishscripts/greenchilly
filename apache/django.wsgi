#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangogolf.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
