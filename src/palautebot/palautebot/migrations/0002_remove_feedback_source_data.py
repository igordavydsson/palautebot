# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palautebot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='source_data',
        ),
    ]