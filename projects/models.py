# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project_Info(models.Model):
    project_name = (models.CharField(max_length=40, null=True))
    project_description = (models.TextField(max_length=200, null=True))
    project_image = (models.ImageField(upload_to="images", null=True))
    project_image_high_res = (models.ImageField(upload_to="images", null=True))

    def __unicode__(self):
        return self.project_name