# Generated by Django 4.1.7 on 2023-03-20 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("std", "0003_remove_subject_is_active_and_more"),
        ("account", "0004_teacher_teaches_in_class"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="teaches",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="teaches",
                to="std.subject",
            ),
        ),
    ]