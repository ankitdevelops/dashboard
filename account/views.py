from django.shortcuts import render, redirect
from .models import User, Student, Teacher
from std.models import Std
from .forms import UserRegisterForm, StudentRegisterForm, TeacherRegisterForm
import datetime
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .custom_decorator import admin_only

# Create your views here.


@admin_only
@login_required(login_url="login")
def add_student(request):
    U_form = UserRegisterForm()
    s_form = StudentRegisterForm()
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        avatar = request.FILES["avatar"]
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        pin_code = request.POST.get("pin_code")
        address = request.POST.get("address")
        std = Std.objects.get(id=request.POST.get("std"))
        guardian_email = request.POST.get("guardian_email")
        guardian_phone_number = request.POST.get("guardian_phone_number")
        guardian_name = request.POST.get("guardian_name")
        admin_no = request.POST.get("admin_no")
        user = User.objects.create(
            first_name=first_name,
            username=f"{first_name}-{dob}",
            last_name=last_name,
            email=email,
            avatar=avatar,
            dob=dob,
            gender=gender,
            city=city,
            pin_code=pin_code,
            address=address,
            password=make_password(f"{first_name}-{dob}"),
            is_student=True,
        )
        student = Student.objects.create(
            user=user,
            guardian_email=guardian_email,
            guardian_phone_number=guardian_phone_number,
            guardian_name=guardian_name,
            admin_no=admin_no,
            std=std,
        )
        user.save()
        student.save()
        return redirect(reverse("class_details", kwargs={"id": std.id}))

    context = {"u_form": U_form, "s_form": s_form}
    return render(request, "account/new_student.html", context)


@admin_only
@login_required(login_url="login")
def add_teacher(request):
    U_form = UserRegisterForm()
    t_form = TeacherRegisterForm()
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        avatar = request.FILES["avatar"]
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        pin_code = request.POST.get("pin_code")
        address = request.POST.get("address")
        qualification = (request.POST.get("qualification"),)
        experience = (request.POST.get("experience"),)
        bio = (request.POST.get("bio"),)
        user = User.objects.create(
            first_name=first_name,
            username=f"{first_name}-{dob}",
            last_name=last_name,
            email=email,
            avatar=avatar,
            dob=dob,
            gender=gender,
            city=city,
            pin_code=pin_code,
            address=address,
            password=make_password(f"{first_name}-{dob}"),
            is_teacher=True,
        )
        teacher = Teacher.objects.create(
            user=user, qualification=qualification, experience=experience, bio=bio
        )
        user.save()
        teacher.save()
        return redirect("home")
    context = {"u_form": U_form, "t_form": t_form}
    return render(request, "account/new_teacher.html", context)


@admin_only
@login_required(login_url="login")
def teacher_details(request):
    teachers = Teacher.objects.all()
    context = {"teachers": teachers}
    return render(request, "account/teacher_details.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Success")
            print("loginsuccess")
            return redirect("home")
        else:
            messages.warning(request, "Invalid Credentials")
            print("something went wrong")
            return redirect("login")
    return render(request, "account/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect("home")
