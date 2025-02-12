#!/usr/bin/env python
import sys
from pathlib import Path

from edc_test_settings.default_test_settings import DefaultTestSettings

app_name = "edc_form_validators"
base_dir = Path(__file__).absolute().parent.parent.parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=str(base_dir / app_name / "tests" / "etc"),
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        "edc_form_validators.apps.AppConfig",
        "form_validators_app.apps.AppConfig",
    ],
).settings

for k, v in project_settings.items():
    setattr(sys.modules[__name__], k, v)
