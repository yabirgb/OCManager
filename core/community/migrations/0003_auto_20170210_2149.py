# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('community', '0002_auto_20170210_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='admins',
        ),
        migrations.AddField(
            model_name='community',
            name='admins',
            field=models.ManyToManyField(related_name='admins', to='users.CustomUser'),
        ),
        migrations.RemoveField(
            model_name='community',
            name='events',
        ),
        migrations.AddField(
            model_name='community',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='events', to='community.Event'),
        ),
        migrations.RemoveField(
            model_name='community',
            name='followers',
        ),
        migrations.AddField(
            model_name='community',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to='users.CustomUser'),
        ),
    ]