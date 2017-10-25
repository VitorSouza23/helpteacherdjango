#-*- coding:UTF-8 -*-
from django import forms

class FormCourse(forms.Form):
    code = forms.IntegerField()
    name = forms.CharField(max_length=264)