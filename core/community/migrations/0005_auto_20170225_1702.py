# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 17:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170225_1702'),
        ('community', '0004_remove_community_followers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser')),
                ('replies', models.ManyToManyField(related_name='_comment_replies_+', to='community.Comment')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='event',
            name='going',
        ),
        migrations.AddField(
            model_name='event',
            name='going',
            field=models.ManyToManyField(related_name='assistants', to='users.CustomUser'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='notGoing',
        ),
        migrations.AddField(
            model_name='event',
            name='notGoing',
            field=models.ManyToManyField(blank=True, related_name='avoiding', to='users.CustomUser'),
        ),
        migrations.AddField(
            model_name='event',
            name='comments',
            field=models.ManyToManyField(blank=True, to='community.Comment'),
        ),
    ]
