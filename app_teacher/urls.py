from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.teacher, name='teacher'),
    url(r'^form_teacher/', views.form_teacher, name='form_teacher'),
    url(r'^delete_teacher/(?P<teacher_id>[0-9]+)/', views.delte_teacher, name='delete_teacher'),
    url(r'^update_teacher/(?P<teacher_id>[0-9]+)/', views.update_teacher, name='update_teacher'),
]