#-*- coding:UTF-8 -*-
from django import forms

class FormTeacher(forms.Form):
    name = forms.CharField(max_length=264, label='Nome:')
    formation = forms.CharField(max_length=264, label='Formação:')
    school = forms.CharField(max_length=264, label='Escola onde trabalha:')