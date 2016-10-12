# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-11 09:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161011_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 10, 11, 9, 47, 20, 717904, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
