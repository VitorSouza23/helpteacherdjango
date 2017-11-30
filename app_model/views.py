# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

import models, forms

# Create your views here.
def grades(request, student_id):
    my_dict = {"grades": models.GradeVO.objects.filter(student__id=student_id), "student": models.StudentVO.objects.get(id=student_id)}
    return render(request, 'app_model/grades.html', context=my_dict)

def classes(request):
    my_dict = {"classes": models.ClassVO.objects.filter(user__id=request.user.id)}
    return render(request, 'app_model/classes.html', context=my_dict)

def courses(request):
    my_dict = {"courses": models.CourseVO.objects.filter(user__id=request.user.id)}
    return render(request, 'app_model/courses.html', context=my_dict)

def students(request):
    my_dict = {"students": models.StudentVO.objects.all()}
    return render(request, 'app_model/students.html', context=my_dict)

def form_course(request):
    form = forms.FormCourse()
    if request.method == "POST":
        form = forms.FormCourse(request.POST)
        if form.is_valid():
            course = models.CourseVO()
            course.code = form.cleaned_data['code']
            course.name = form.cleaned_data['name']
            course.user = request.user
            course.save()
            return HttpResponseRedirect('/app_model/courses/')

    return render(request, 'app_model/form_course.html', {'form': form})

def delete_course(request, course_id):
    course = models.CourseVO.objects.get(id=course_id)
    course.delete()
    return HttpResponseRedirect('/app_model/courses/')

def update_course(request, course_id):
    course = models.CourseVO.objects.get(id=course_id)
    form = forms.FormCourse(initial={'code': course.code, 'name': course.name})
    if request.method == "POST":
        form = forms.FormCourse(request.POST)
        if form.is_valid():
            course.code = form.cleaned_data['code']
            course.name = form.cleaned_data['name']
            course.save()
            return HttpResponseRedirect('/app_model/courses/')

    return render(request, 'app_model/form_course.html', {'form': form}) 


def form_class(request):
    form = forms.FormClass(request.user)
    if request.method == "POST":
        form = forms.FormClass(request.user,request.POST)
        if form.is_valid():
            classvo = models.ClassVO()
            classvo.code = form.cleaned_data['code']
            classvo.name = form.cleaned_data['name']
            classvo.course = form.cleaned_data['course']
            classvo.discipline = form.cleaned_data['discipline']
            classvo.schedule = form.cleaned_data['schedule']
            classvo.user = request.user
            classvo.save()
            return HttpResponseRedirect('/app_model/classes/')
    
    return render(request, 'app_model/form_class.html', {'form': form})

def delete_class(request, class_id):
    classvo = models.ClassVO.objects.get(id=class_id)
    classvo.delete()
    return HttpResponseRedirect('/app_model/classes/')

def update_class(request, class_id):
    classvo = models.ClassVO.objects.get(id=class_id)
    form = forms.FormClass(request.user,initial={'code': classvo.code, 'name': classvo.name, 'discipline': classvo.discipline, 'schedule': classvo.schedule.strftime('%H:%M'), 'course': classvo.course})
    if request.method == "POST":
        form = forms.FormCourse(request.user,request.POST)
        if form.is_valid():
            classvo.code = form.cleaned_data['code']
            classvo.name = form.cleaned_data['name']
            classvo.course = form.cleaned_data['course']
            classvo.discipline = form.cleaned_data['discipline']
            classvo.schedule = form.cleaned_data['schedule']
            course.save()
            return HttpResponseRedirect('/app_model/classes/')

    return render(request, 'app_model/form_class.html', {'form': form}) 

def form_student(request):
    form = forms.FormStudent()
    if request.method == "POST":
        form = forms.FormStudent(request.POST)
        if form.is_valid():
            student = models.StudentVO()
            student.name = form.cleaned_data['name']
            student.registration = form.cleaned_data['registration']
            student.class_scholl = form.cleaned_data['class_scholl']
            student.save()
            return HttpResponseRedirect('/app_model/students/')

    return render(request, 'app_model/form_student.html', {'form': form})

def delete_student(request, student_id):
    student = models.StudentVO.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect('/app_model/students/')

def update_student(request, student_id):
    student = models.StudentVO.objects.get(id=student_id)
    form = forms.FormStudent(initial={'name': student.name, 'registration': student.registration, 'class_scholl': student.class_scholl})
    if request.method == "POST":
        form = forms.FormStudent(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.registration = form.cleaned_data['registration']
            student.class_scholl = form.cleaned_data['class_scholl']
            student.save()
            return HttpResponseRedirect('/app_model/students/')

    return render(request, 'app_model/form_student.html', {'form': form})

def form_grade(request, student_id):
    form = forms.FormGrade()
    if request.method == "POST":
        form = forms.FormGrade(request.POST)
        if form.is_valid():
            grade = models.GradeVO()
            grade.value = form.cleaned_data['value']
            grade.observation = form.cleaned_data['observation']
            grade.student = models.StudentVO.objects.get(id=student_id)
            grade.save()
            return HttpResponseRedirect('/app_model/grades/'+student_id)

    return render(request, 'app_model/form_grade.html', {'form': form})

def delete_grade(request, student_id, grade_id):
    grade = models.GradeVO.objects.get(id=grade_id)
    grade.delete()
    return HttpResponseRedirect('/app_model/grades/'+student_id)

def update_grade(request, student_id, grade_id):
    grade = models.GradeVO.objects.get(id=grade_id)
    form = forms.FormGrade(initial={'value': grade.value, 'observation': grade.observation})
    if request.method == "POST":
        form = forms.FormGrade(request.POST)
        if form.is_valid():
            grade.value = form.cleaned_data['value']
            grade.observation = form.cleaned_data['observation']
            grade.save()
            return HttpResponseRedirect('/app_model/grades/'+student_id)

    return render(request, 'app_model/form_grade.html', {'form': form})         

