# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project_Info(models.Model):
    project_name = (models.CharField(max_length=40, null=True))
    project_description = (models.TextField(max_length=1000, null=True))
    project_image = (models.ImageField(upload_to="images", null=True))
    project_image_high_res = (models.ImageField(upload_to="images", null=True))
    project_git = (models.CharField(max_length=100, null=True))
    project_link = (models.CharField(max_length=100, null=True))

    def __unicode__(self):
        return self.project_name
