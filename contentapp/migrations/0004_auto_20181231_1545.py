# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-31 12:45
from __future__ import unicode_literals

import contentapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0003_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя слайда')),
                ('image', models.ImageField(upload_to=contentapp.models.upload_slides)),
            ],
        ),
        migrations.AlterModelOptions(
            name='files',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]