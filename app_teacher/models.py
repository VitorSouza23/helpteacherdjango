# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TeacherVO(models.Model):
    name = models.CharField(max_length=264)
    formation = models.CharField(max_length=264)
    school = models.CharField(max_length=264)