from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.teacher, name='teacher'),
    url(r'^form_teacher/', views.form_teacher, name='form_teacher'),
    url(r'^delete_teacher/', views.delte_teacher, name='delete_teacher')
]