# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseVO(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=264)

class ClassVO(models.Model):
    code = models.IntegerField()
    discipline = models.CharField(max_length=264)
    name = models.CharField(max_length=264)
    schedule = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(CourseVO)

class StudentVO(models.Model):
    registration = models.IntegerField()
    name = models.CharField(max_length=264)
    class_scholl = models.ForeignKey(ClassVO)

class GradeVO(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2)
    observation = models.CharField(max_length=264)
    student = models.ForeignKey(StudentVO)