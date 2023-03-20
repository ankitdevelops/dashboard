# Generated by Django 4.1.7 on 2023-03-19 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("std", "0002_rename_lesson_topic"),
        ("account", "0002_student_std"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="std",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="learning_in_class",
                to="std.std",
            ),
        ),
    ]