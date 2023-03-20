from django import forms
from .models import User, Student, Teacher


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

        widgets = {
            "dob": forms.DateInput(attrs={"class": "form-control ", "type": "date"})
        }


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "guardian_email",
            "guardian_phone_number",
            "guardian_name",
            "admin_no",
            "class_roll_no",
            "std",
        ]


class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["qualification", "experience", "bio"]
