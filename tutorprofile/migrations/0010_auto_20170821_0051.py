# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0009_tutorprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorprofile',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]