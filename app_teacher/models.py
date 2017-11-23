# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class TeacherVO(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=264)
    formation = models.CharField(max_length=264)
    school = models.CharField(max_length=264)