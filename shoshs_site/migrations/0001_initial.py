# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graphic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphic_image', models.ImageField(upload_to=b'graphic_images')),
                ('graphic_image_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=25)),
                ('website_url', models.CharField(max_length=100)),
            ],
        ),
    ]