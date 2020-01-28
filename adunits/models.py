from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from adunits import signals as adunit_signals


class Vendor(models.Model):
    name = models.CharField(unique=True, max_length=30)
    header_source = models.TextField(
        null=True, blank=True,
        help_text="Commonly, scripts are needed between <head></head>")
    endbody_source = models.TextField(
        null=True, blank=True,
        help_text="Commonly scripts are needed before </body>")

    def __unicode__(self):
        return self.name


class Unit(models.Model):
    vendor = models.ForeignKey('Vendor', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,)
    source = models.TextField(
        help_text="html/script source. generally you're 'ad tags'")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('vendor', 'name',)


class Settings(models.Model):
    site = models.OneToOneField('sites.Site', null=True, blank=True, on_delete=models.PROTECT)
    active_vendor = models.OneToOneField('Vendor', null=True, blank=True)
    header_source = models.TextField(
        null=True, blank=True,
        help_text="Commonly, scripts are needed between <head></head>")
    endbody_source = models.TextField(
        null=True, blank=True,
        help_text="Commonly scripts are needed before </body>")

    def __unicode__(self):
        tokens = []
        if self.site_id:
            tokens.append(self.site)
        if self.active_vendor:
            tokens.append(self.active_vendor)
        return " - ".join(map(str, tokens))


signals.post_migrate.connect(
    adunit_signals.create_initial_settings, sender=Settings)
