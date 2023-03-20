from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# from std.models import Std

# signals import
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Others"

    phone = models.CharField(max_length=60)
    city = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField()
    avatar = models.ImageField(
        upload_to="user/picture/%Y/%m/", default="default.png", blank=True, null=True
    )
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices)

    def get_avatar_url(self):
        return self.avatar.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 300 or img.width > 300:
                img_size = (300, 300)
                img.thumbnail(img_size)
                img.save(self.avatar.path)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teachers")
    qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=20)
    bio = models.CharField(max_length=250)
    is_class_head = models.BooleanField(default=False)
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    guardian_email = models.EmailField(max_length=250, blank=True, null=True)
    guardian_phone_number = models.CharField(max_length=50, blank=True, null=True)
    guardian_name = models.CharField(max_length=50, blank=True, null=True)
    is_ta = models.BooleanField(default=False)
    admin_no = models.CharField(max_length=10)
    class_roll_no = models.CharField(max_length=5)
    std = models.ForeignKey(
        "std.Std",
        on_delete=models.SET_NULL,
        null=True,
        related_name="learning_in_class",
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print(kwargs)
#         # Student.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
