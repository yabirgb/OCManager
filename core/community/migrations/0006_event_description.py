# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20170225_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
