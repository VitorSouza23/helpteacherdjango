from django.conf.urls import url
import views

urlpatterns = [
    url(r'^grades/', views.grades, name='grades'),
    url(r'^classes/', views.classes, name='classes'),
    url(r'^courses/', views.courses, name='courses'),
    url(r'^students/', views.students, name='students'),
]