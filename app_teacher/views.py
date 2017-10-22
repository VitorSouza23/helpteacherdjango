# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

import models, forms

# Create your views here.
def teacher(request):
    my_dict = {"teachers": models.TeacherVO.objects.all(), "selected_teacher": models.TeacherVO.objects.first()}
    return render(request, 'app_teacher/teacher.html', context=my_dict)

def form_teacher(request):
    form = forms.FormTeacher()
    if request.method == "POST":
        form = forms.FormTeacher(request.POST)
        
        if form.is_valid():
            teacher = models.TeacherVO()
            teacher.name = form.cleaned_data['name']
            teacher.formation = form.cleaned_data['formation']
            teacher.school = form.cleaned_data['school']
            teacher.save()
            return HttpResponseRedirect('/app_teacher/')

    return render(request, 'app_teacher/form_teacher.html', {'form': form})

def delte_teacher(request, teacher_id):
    teacher = models.TeacherVO.objects.get(id=teacher_id)
    teacher.delete()
    return HttpResponseRedirect('/app_teacher/')