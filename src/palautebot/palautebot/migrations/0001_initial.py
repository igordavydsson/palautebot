# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=2048)),
                ('source_id', models.CharField(max_length=2048, unique=True)),
                ('source_type', models.CharField(choices=[('twitter', 'Twitter'), ('instagram', 'Facebook'), ('facebook', 'Facebook')], max_length=2048)),
                ('source_data', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]