from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("NAME_LOCAL"),
        "USER": os.environ.get("USER_LOCAL"),
        "PASSWORD": os.environ.get("PASSWORD_LOCAL"),
        "HOST": os.environ.get("HOST_LOCAL"),
        "PORT": os.environ.get("PORT_LOCAL"),
    }
}
