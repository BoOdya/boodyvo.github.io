# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20160813_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
