#-*- coding:UTF-8 -*-
from django import forms
import models

class FormCourse(forms.Form):
    code = forms.IntegerField(label='Código')
    name = forms.CharField(max_length=264, label="Nome do Curso")

class FormClass(forms.Form):
    def _inti_(self, user):
        self.user = user

    code = forms.IntegerField(label='Código')
    discipline = forms.CharField(max_length=264, label='Disciplina')
    name = forms.CharField(max_length=264, label='Nome (Identificador) da Turma')
    schedule = forms.DateTimeField(['%H:%M'], label="Horário da Aula (HH:MM):")
    course = forms.ModelChoiceField(queryset=models.CourseVO.objects.filter(user__id=self.user.id), label='Curso')

class FormStudent(forms.Form):
    registration = forms.IntegerField(label='Matrícula')
    name = forms.CharField(max_length=264, label='Nome')
    class_scholl = forms.ModelChoiceField(queryset=models.ClassVO.objects.all(), label='Turma')

class FormGrade(forms.Form):
    value = forms.DecimalField(max_digits=4, decimal_places=2, label='Valor')
    observation = forms.CharField(max_length=264, label='Observação')