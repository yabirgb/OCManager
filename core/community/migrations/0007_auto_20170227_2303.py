# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='id',
        ),
        migrations.AddField(
            model_name='community',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
