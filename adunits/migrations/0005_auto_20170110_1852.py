# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-10 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adunits', '0004_auto_20160920_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='site',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
