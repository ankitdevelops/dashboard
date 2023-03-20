from django.shortcuts import render, redirect
from .models import Std, Student, Teacher, Subject, Chapters, Topic, Assignment
from .forms import (
    UserRegisterForm,
    StudentRegisterForm,
    SubjectForm,
    ChapterForm,
    STDForm,
    TopicForm,
    AssignmentCreateForm,
    AssignmentSubmitForm,
)
from django.contrib.auth.decorators import login_required
from account.custom_decorator import admin_only
from django.urls import reverse
from .custom_decorator import teacher_only

# Create your views here.


@admin_only
@login_required(login_url="login")
def add_std(request):
    form = STDForm()
    if request.method == "POST":
        form = STDForm(request.POST)
        teacher_id = request.POST.get("class_head")
        teacher = teacher = Teacher.objects.get(id=teacher_id)
        teacher.is_class_head = True

        if form.is_valid():
            form.save()
            teacher.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "std/add_class.html", context)


@admin_only
@login_required(login_url="login")
def class_details(request, id):
    std = Std.objects.get(id=id)
    students = Student.objects.filter(std=std)
    print(students)
    context = {"std": std, "students": students}
    return render(request, "std/class_details.html", context)


@admin_only
@login_required(login_url="login")
def add_new_subject(request, id):
    std = Std.objects.get(id=id)
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.class_id = std
            formdata.save()
            return redirect("home")
    context = {"form": form, "std": std}
    return render(request, "std/add_new_subject.html", context)


def subject_details(request, id):
    subject = Subject.objects.get(id=id)
    chapters = Chapters.objects.filter(subject=subject)
    context = {"subject": subject, "chapters": chapters}
    return render(request, "std/subject_details.html", context)


def topic_details(request, id):
    topic = Topic.objects.get(id=id)
    context = {"topic": topic}
    return render(request, "std/topic_details.html", context)


@teacher_only
def add_chapter(request, id):
    subject = Subject.objects.get(id=id)
    form = ChapterForm()
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.subject = subject
            form_data.save()
            return redirect(reverse("subject_details", kwargs={"id": subject.id}))

    context = {"form": form, "subject": subject}

    return render(request, "std/add_chapter.html", context)


@teacher_only
def add_topic(request, id):
    chapter = Chapters.objects.get(id=id)
    form = TopicForm()
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.chapter = chapter
            form_data.save()
            return redirect("home")
    context = {"form": form, "chapter": chapter}
    return render(request, "std/add_new_topic.html", context)


def add_assignment(request, chapterId, subjectId):
    chapter = Chapters.objects.get(id=chapterId)

    subject = Subject.objects.get(id=subjectId)
    std = Std.objects.get(id=subject.class_id.id)
    form = AssignmentCreateForm()
    if request.method == "POST":
        form = AssignmentCreateForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.chapter = chapter
            form_data.subject = subject
            form_data.class_id = std
            form_data.save()
            return redirect(reverse("subject_details", kwargs={"id": subject.id}))

    context = {
        "form": form,
        "chapter": chapter,
        "subject": subject,
    }
    return render(request, "std/add_assignment.html", context)


def show_assignment(request, chapterId):
    chapter = Chapters.objects.get(id=chapterId)
    assignments = Assignment.objects.filter(chapter=chapter.id).order_by("-created_at")
    context = {"assignments": assignments, "chapter": chapter}
    return render(request, "std/assignment.html", context)


def submit_assignment(request, id, chId):
    student = Student.objects.get(user=request.user)
    assignment = Assignment.objects.get(id=id)
    chapter = Chapters.objects.get(id=chId)
    if request.method == "POST":
        form = AssignmentSubmitForm(request.POST, instance=assignment)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.submitted_by = student
            form_data.save()
            return redirect(reverse("assignments", kwargs={"chapterId": chapter.id}))
    form = AssignmentSubmitForm(instance=assignment)
    context = {"assignment": assignment, "form": form, "chapter": chapter}
    return render(request, "std/submit_assignment.html", context)
