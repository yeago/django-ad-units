# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adunits', '0003_vendor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together=set([('vendor', 'name')]),
        ),
    ]
