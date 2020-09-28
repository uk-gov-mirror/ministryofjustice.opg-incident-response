import logging
import os

from django.core.exceptions import ImproperlyConfigured

from response.slack.client import SlackClient

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "after_response",
    "rest_framework",
    "bootstrap4",
    "response.apps.ResponseConfig",
    'health_check',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "opgincidentresponse.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "opgincidentresponse.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Django Rest Framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    # Use Django's standard `django.contrib.auth` permissions.
    # Change to IsAuthenticatedOrReadOnly for read-only unauthenticated access
    # or see the Django Rest Framework docs for more options:
    # https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
}

# Markdown Filter

MARKDOWN_FILTER_WHITELIST_TAGS = [
    "a",
    "p",
    "code",
    "h1",
    "h2",
    "ul",
    "li",
    "strong",
    "em",
    "img",
]

MARKDOWN_FILTER_WHITELIST_ATTRIBUTES = ["src", "style"]

MARKDOWN_FILTER_WHITELIST_STYLES = [
    "width",
    "height",
    "border-color",
    "background-color",
    "white-space",
    "vertical-align",
    "text-align",
    "border-style",
    "border-width",
    "float",
    "margin",
    "margin-bottom",
    "margin-left",
    "margin-right",
    "margin-top",
]


def get_env_var(setting, warn_only=False):
    value = os.getenv(setting, None)

    if not value:
        error_msg = f"ImproperlyConfigured: Set {setting} environment variable"
        if warn_only:
            logger.warn(error_msg)
        else:
            raise ImproperlyConfigured(error_msg)
    else:
        value = value.replace('"', "")  # remove start/end quotes

    return value


SLACK_TOKEN = get_env_var("SLACK_TOKEN")
SLACK_CLIENT = SlackClient(SLACK_TOKEN)


# Whether to use https://pypi.org/project/bleach/ to strip potentially dangerous
# HTML input in string fields
RESPONSE_SANITIZE_USER_INPUT = True
