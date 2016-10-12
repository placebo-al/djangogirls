from mysite.settings import *
import dj_database_url

DATABASES = {
    "default": dj_database_url.config(default='postgres://localhost'),
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE ='whitenoise.django.GzipManifestStaticFilesStorage'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        }
    }
}