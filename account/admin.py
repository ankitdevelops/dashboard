from django.contrib import admin
from .models import User, Teacher, Student


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "is_student",
        "is_teacher",
    ]
    list_filter = ["username", "is_student", "is_teacher"]


admin.site.register(Teacher)
admin.site.register(Student)
