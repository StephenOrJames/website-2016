# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_remove_newsletter_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
            options={
                'db_table': 'ideas',
                'verbose_name_plural': 'Idea Machines',
                'verbose_name': 'Idea Machine',
            },
        ),
    ]
