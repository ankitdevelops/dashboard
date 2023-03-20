from django.shortcuts import render, redirect
from std.models import Std, Subject
from account.models import Teacher, Student
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def home(request):
    if request.user.is_teacher:
        teacher = Teacher.objects.get(user=request.user)
        subjects = Subject.objects.filter(faculty=teacher)
        std = Std.objects.get(class_head=teacher)
        students = Student.objects.filter(std=std)

        context = {"subjects": subjects, "teacher": teacher, "students": students}

    if request.user.is_superuser:
        total_student = Student.objects.all().count()
        total_teacher = Teacher.objects.all().count()
        teachers = Teacher.objects.all()
        students = Student.objects.all()
        context = {
            "total_student": total_student,
            "total_teacher": total_teacher,
            "teachers": teachers,
            "students": students,
        }
    if request.user.is_student:
        student = Student.objects.get(user=request.user)
        std = Std.objects.get(id=student.std.id)
        subjects = Subject.objects.filter(class_id=std.id)
        context = {"subjects": subjects, "student": student, "std": std}

    return render(request, "home.html", context)
