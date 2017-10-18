from django.conf.urls import url
import views

urlpatterns = [
    url(r'^grades/', views.grades, name='grades'),
    url(r'^classes/', views.classes, name='grades'),
    url(r'^courses/', views.courses, name='grades'),
    url(r'^students/', views.students, name='grades'),
]