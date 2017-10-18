# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def teacher(request):
    my_dict = {}
    return render(request, 'app_teacher/teacher.html', context=my_dict)