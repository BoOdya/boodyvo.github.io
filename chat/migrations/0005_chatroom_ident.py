# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20160809_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='ident',
            field=models.TextField(default=None),
        ),
    ]
