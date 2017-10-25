# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app_model import models

admin.site.register(models.ClassVO)
admin.site.register(models.CourseVO)
admin.site.register(models.GradeVO)
admin.site.register(models.StudentVO)