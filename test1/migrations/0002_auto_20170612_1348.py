# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-12 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finger_tmp',
            name='TMP',
            field=models.CharField(max_length=4000),
        ),
    ]
