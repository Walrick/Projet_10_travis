"""
WSGI config for pur_beurre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


def env_setting():
    # open file .env for set setting
    with open(".env", "r") as file:
        lines = file.readlines()
    for line in lines:
        lg = line.split(" ")
        word_list = []
        # remove "\n"
        for letter in lg[2]:
            if "\n" != letter:
                word_list.append(letter)
        word = "".join(word_list)
        # append key in os
        os.environ[lg[0]] = word

try:
    env_setting()
except:
    print("no fichier .env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pur_beurre.settings.production")

application = get_wsgi_application()

