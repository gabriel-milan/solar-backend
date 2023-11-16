# -*- coding: utf-8 -*-
from . import getenv_list_or_action, getenv_or_action

# Database configuration
DATABASE_URL = getenv_or_action("DATABASE_URL", action="raise")

# CORS configuration
ALLOWED_ORIGINS = getenv_list_or_action("ALLOWED_ORIGINS", action="ignore")
ALLOWED_ORIGINS_REGEX = None
if not ALLOWED_ORIGINS and not ALLOWED_ORIGINS_REGEX:
    raise EnvironmentError("ALLOWED_ORIGINS or ALLOWED_ORIGINS_REGEX must be set.")
ALLOWED_METHODS = getenv_list_or_action("ALLOWED_METHODS", action="raise")
ALLOWED_HEADERS = getenv_list_or_action("ALLOWED_HEADERS", action="raise")
ALLOW_CREDENTIALS = getenv_or_action("ALLOW_CREDENTIALS", action="raise").lower() == "true"
