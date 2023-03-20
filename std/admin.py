from django.contrib import admin
from .models import Std, Subject, Chapters, Topic, Assignment

# Register your models here.
admin.site.register(Std)
admin.site.register(Subject)
admin.site.register(Chapters)
admin.site.register(Topic)
admin.site.register(Assignment)
