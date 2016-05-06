from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.contrib import sites
from adunits import signals as adunit_signals


class Unit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    source = models.TextField(
        help_text="html/script source. generally you're 'ad tags'")
    date_added = models.DateTimeField(auto_now_add=True)


class Settings(models.Model):
    site = models.OneToOneField('sites.Site')
    header_source = models.TextField(
        null=True, blank=True,
        help_text="Commonly, scripts are needed between <head></head>")
    endbody_source = models.TextField(
        null=True, blank=True,
        help_text="Commonly scripts are needed before </body>")


signals.post_migrate.connect(
    adunit_signals.create_initial_settings, sender=Settings)
