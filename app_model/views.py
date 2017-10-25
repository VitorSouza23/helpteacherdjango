# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

import models, forms

# Create your views here.
def grades(request):
    my_dict = {}
    return render(request, 'app_model/grades.html', context=my_dict)

def classes(request):
    my_dict = {}
    return render(request, 'app_model/classes.html', context=my_dict)

def courses(request):
    my_dict = {"courses": models.CourseVO.objects.all()}
    return render(request, 'app_model/courses.html', context=my_dict)

def students(request):
    my_dict = {}
    return render(request, 'app_model/students.html', context=my_dict)

def form_course(request):
    form = forms.FormCourse()
    if request.method == "POST":
        form = forms.FormCourse(request.POST)
        if form.is_valid():
            course = models.CourseVO()
            course.code = form.cleaned_data['code']
            course.name = form.cleaned_data['name']
            course.save()
            return HttpResponseRedirect('/app_model/courses/')

    return render(request, 'app_model/form_course.html', {'form': form})