#!/home/pi/.virtualenvs/env/bin/python
# -*- coding: utf-8 -*-
"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bin.core.settings")


## VECCHIA GESTIONE
## TODO: DA RIVEDERE
# if 'OPENSHIFT_REPO_DIR' in os.environ:
# sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'core'))
#     virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
#     os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
#     virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
#     try:
#         with open(virtualenv, 'rb') as exec_file:
#             file_contents = exec_file.read()
#         compiled_code = compile(file_contents, virtualenv, 'exec')
#         exec_namespace = dict(__file__=virtualenv)
#         exec(compiled_code, exec_namespace)
#     except IOError:
#         pass


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
