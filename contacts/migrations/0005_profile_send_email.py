# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20160411_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='send_email',
            field=models.BooleanField(default=True),
        ),
    ]
