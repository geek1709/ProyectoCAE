# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_registroclie'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroclie',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
