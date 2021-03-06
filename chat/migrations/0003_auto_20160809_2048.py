# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_chatmessage_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='mainUser',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='mainUser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mainUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='secondaryUser',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='secondaryUser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='secondaryUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
