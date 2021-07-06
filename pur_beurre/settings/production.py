from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

travis = os.environ.get("TRAVIS", False)
# Test mode for Travis
if travis == "TRUE":
    ALLOWED_HOSTS = ["127.0.0.1"]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("myapp_test"),
            "USER": os.environ.get("travis"),
            "PASSWORD": os.environ.get(""),
            "HOST": os.environ.get("localhost"),
            "PORT": os.environ.get("3306"),
        }
    }
# Product mode
else:
    ALLOWED_HOSTS = ["217.160.27.219"]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("NAME_SERVER"),
            "USER": os.environ.get("USER_SERVER"),
            "PASSWORD": os.environ.get("PASSWORD_SERVER"),
            "HOST": os.environ.get("HOST_SERVER"),
            "PORT": os.environ.get("PORT_SERVER"),
        }
    }


# Static files settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, "staticfiles")

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
