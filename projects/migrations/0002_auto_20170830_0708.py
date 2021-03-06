# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_info',
            name='project_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project_info',
            name='project_description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project_info',
            name='project_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
