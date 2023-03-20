from django.urls import path
from . import views

urlpatterns = [
    path("add_student/", views.add_student, name="add_student"),
    path("add_teacher/", views.add_teacher, name="add_teacher"),
    path("teacher_details/", views.teacher_details, name="teacher_details"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_user, name="logout_user"),
]
