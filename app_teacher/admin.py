# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app_teacher.models import TeacherVO

admin.site.register(TeacherVO)