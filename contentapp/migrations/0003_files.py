# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-29 19:58
from __future__ import unicode_literals

import contentapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0002_auto_20181227_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя файла')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание файла')),
                ('file', models.FileField(upload_to=contentapp.models.upload_files, verbose_name='Файл')),
            ],
        ),
    ]
