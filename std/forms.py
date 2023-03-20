from django import forms
from .models import Std, Subject, Chapters, Topic, Assignment
from account.models import User, Student
from ckeditor.widgets import CKEditorWidget


class STDForm(forms.ModelForm):
    class Meta:
        model = Std
        fields = ["class_name", "class_head"]


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "avatar",
            "dob",
            "gender",
            "city",
            "pin_code",
            "address",
        ]


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "guardian_email",
            "guardian_phone_number",
            "guardian_name",
            "admin_no",
            "class_roll_no",
        ]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_name", "subject_code", "description", "faculty"]


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapters
        fields = ["title", "description"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "content_type", "video_id", "text_content", "pdf"]


class AssignmentCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Assignment
        fields = ["content"]
        help_texts = {
            "content": None,
        }


class AssignmentSubmitForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Assignment
        fields = ["answer"]
        exclude = ("content",)
        help_texts = {
            "answer": None,
        }
