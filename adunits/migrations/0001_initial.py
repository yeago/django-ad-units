# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_source', models.TextField(blank=True, help_text='Commonly, scripts are needed between <head></head>', null=True)),
                ('endbody_source', models.TextField(blank=True, help_text='Commonly scripts are needed before </body>', null=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('source', models.TextField(help_text="html/script source. generally you're 'ad tags'")),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
