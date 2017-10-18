# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def grades(request):
    my_dict = {}
    return render(request, 'app_model/grades.html', context=my_dict)

def classes(request):
    my_dict = {}
    return render(request, 'app_model/classes.html', context=my_dict)

def courses(request):
    my_dict = {}
    return render(request, 'app_model/courses.html', context=my_dict)

def students(request):
    my_dict = {}
    return render(request, 'app_model/students.html', context=my_dict)