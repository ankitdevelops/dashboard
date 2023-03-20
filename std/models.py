from django.db import models
from account.models import Student, Teacher
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Std(models.Model):
    class_name = models.CharField(max_length=50)
    class_head = models.OneToOneField(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name="class_head_teacher",
    )
    students = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, related_name="class_students"
    )

    def __str__(self):
        return self.class_name

    def total_student_count(self):
        return self.students.class_students.count()

    def get_url(self):
        return reverse("class_details", args=[self.id])


class Subject(models.Model):
    class_id = models.ForeignKey(
        Std, on_delete=models.CASCADE, related_name="class_subjects"
    )
    subject_name = models.CharField(max_length=250)
    subject_code = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField()
    faculty = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subject_teacher",
    )

    def __str__(self):
        return f"{self.subject_name} - {self.subject_code}"


class Chapters(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_chapters"
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    last_updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    class ContentType(models.TextChoices):
        YT_VIDEO = "YT_VIDEO", "YouTube Video"
        VIMEO_VIDEO = "VIMEO_VIDEO", "Vimeo Video"
        PDF = "PDF", "PDF"
        TEXT = "TEXT", "TEXT"

    chapter = models.ForeignKey(
        Chapters, on_delete=models.CASCADE, related_name="topics"
    )
    title = models.CharField(max_length=250)
    content_type = models.CharField(
        max_length=50, choices=ContentType.choices, default=ContentType.YT_VIDEO
    )
    video_id = models.CharField(max_length=100, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    pdf = models.FileField(upload_to="pdf/%Y/%m/", blank=True, null=True)

    def clean(self):
        if self.content_type == "YT_VIDEO" and self.video_id == None:
            raise ValidationError("YouTube Video Link Not Found")
        if self.content_type == "VIMEO_VIDEO" and self.video_id == None:
            raise ValidationError("Vimeo Video Link Not Found")
        if self.content_type == "TEXT" and self.text_content == "":
            raise ValidationError("Text Content Can't be empty")
        if self.content_type == "PDF" and self.pdf == None:
            raise ValidationError("No pdf file found")

    # def save(self, *args, **kwargs):
    #     print(self.)
    #     super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.chapter.title} -- {self.title}"


class Assignment(models.Model):
    class_id = models.ForeignKey(
        Std, on_delete=models.CASCADE, related_name="assignment_of_class"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="assignment_of_subject"
    )
    chapter = models.ForeignKey(
        Chapters,
        on_delete=models.CASCADE,
        related_name="assignment_of_chapter",
        blank=True,
        null=True,
    )

    content = RichTextField()

    answer = RichTextField(blank=True, null=True)
    submitted_by = models.ForeignKey(
        Student, on_delete=models.SET_NULL, blank=True, null=True
    )

    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Assignment for {self.class_id} of {self.subject}"
