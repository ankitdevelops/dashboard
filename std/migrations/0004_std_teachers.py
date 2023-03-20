# Generated by Django 4.1.7 on 2023-03-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0006_remove_teacher_teaches_in_class"),
        ("std", "0003_remove_subject_is_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="std",
            name="teachers",
            field=models.ManyToManyField(blank=True, null=True, to="account.teacher"),
        ),
    ]