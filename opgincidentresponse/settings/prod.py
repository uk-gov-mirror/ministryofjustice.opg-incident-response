import os

from .base import *  # noqa: F401, F403
from .base import SLACK_CLIENT, get_env_var

SITE_URL = os.environ.get("SITE_URL")

DEBUG = False

if os.environ.get("POSTGRES"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
            "USER": os.environ.get("DB_USER"),
            "NAME": os.environ.get("DB_NAME"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "OPTIONS": {"sslmode": os.getenv("DB_SSL_MODE", "disable")},
        }
    }

SLACK_TOKEN = get_env_var("SLACK_TOKEN")
SLACK_SIGNING_SECRET = get_env_var("SLACK_SIGNING_SECRET")
SLACK_TEAM_ID = get_env_var("SLACK_TEAM_ID")
INCIDENT_CHANNEL_NAME = get_env_var("INCIDENT_CHANNEL_NAME")
INCIDENT_REPORT_CHANNEL_NAME = get_env_var("INCIDENT_REPORT_CHANNEL_NAME")
INCIDENT_BOT_NAME = get_env_var("INCIDENT_BOT_NAME")

INCIDENT_BOT_ID = os.getenv("INCIDENT_BOT_ID") or SLACK_CLIENT.get_user_id(
    INCIDENT_BOT_NAME
)
INCIDENT_CHANNEL_ID = os.getenv("INCIDENT_CHANNEL_ID") or SLACK_CLIENT.get_channel_id(
    INCIDENT_CHANNEL_NAME
)
INCIDENT_REPORT_CHANNEL_ID = os.getenv(
    "INCIDENT_REPORT_CHANNEL_ID"
) or SLACK_CLIENT.get_channel_id(INCIDENT_REPORT_CHANNEL_NAME)

STATUSPAGEIO_API_KEY = get_env_var("STATUSPAGEIO_API_KEY")
STATUSPAGEIO_PAGE_ID = get_env_var("STATUSPAGEIO_PAGE_ID")
PAGERDUTY_API_KEY = get_env_var("PAGERDUTY_API_KEY")
PAGERDUTY_SERVICE = get_env_var("PAGERDUTY_SERVICE")
PAGERDUTY_EMAIL = get_env_var("PAGERDUTY_EMAIL")
