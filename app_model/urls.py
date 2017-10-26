from django.conf.urls import url
import views

urlpatterns = [
    url(r'^grades/(?P<student_id>[0-9]+)', views.grades, name='grades'),
    url(r'^form_grade/(?P<student_id>[0-9]+)/', views.form_grade, name='form_grade'),
    url(r'^delete_grade/(?P<student_id>[0-9]+)/(?P<grade_id>[0-9]+)/', views.delete_grade, name='delete_grade'),
    url(r'^update_grade/(?P<student_id>[0-9]+)/(?P<grade_id>[0-9]+)/', views.update_grade, name='update_grade'),
    url(r'^classes/', views.classes, name='classes'),
    url(r'^form_class/', views.form_class, name='form_class'),
    url(r'^delete_class/(?P<class_id>[0-9]+)/', views.delete_class, name='delete_class'),
    url(r'^update_class/(?P<class_id>[0-9]+)/', views.update_class, name='update_class'),
    url(r'^courses/', views.courses, name='courses'),
    url(r'^form_course/', views.form_course, name='form_course'),
    url(r'^delete_course/(?P<course_id>[0-9]+)/', views.delete_course, name='delete_course'),
    url(r'^update_course/(?P<course_id>[0-9]+)/', views.update_course, name='update_course'),
    url(r'^students/', views.students, name='students'),
    url(r'^form_student/', views.form_student, name='form_student'),
    url(r'^delete_student/(?P<student_id>[0-9]+)/', views.delete_student, name='delete_student'),
    url(r'^update_student/(?P<student_id>[0-9]+)/', views.update_student, name='update_student'),
]