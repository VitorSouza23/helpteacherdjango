# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.

class CourseVO(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=264)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class ClassVO(models.Model):
    code = models.IntegerField()
    discipline = models.CharField(max_length=264)
    name = models.CharField(max_length=264)
    schedule = models.DateTimeField(['%H:%M'])
    course = models.ForeignKey(CourseVO)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class StudentVO(models.Model):
    registration = models.IntegerField()
    name = models.CharField(max_length=264)
    class_scholl = models.ForeignKey(ClassVO)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class GradeVO(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2)
    observation = models.CharField(max_length=264)
    student = models.ForeignKey(StudentVO)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)