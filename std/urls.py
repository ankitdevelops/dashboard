from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.class_details, name="class_details"),
    path("add_class/", views.add_std, name="add-std"),
    path("<int:id>/add_new_subject", views.add_new_subject, name="add_new_subject"),
    path("subject_details/<int:id>/", views.subject_details, name="subject_details"),
    path("add_chapter/<int:id>/", views.add_chapter, name="add_chapter"),
    path("topic_details/<int:id>/", views.topic_details, name="topic_details"),
    path("chapter/<int:id>/add_topic/", views.add_topic, name="add_topic"),
    path(
        "assignment/<int:subjectId>/<int:chapterId>/",
        views.add_assignment,
        name="add_new_assignment",
    ),
    path("show_assignment/<int:chapterId>/", views.show_assignment, name="assignments"),
    path(
        "submit_assignment/<int:chId>/<int:id>/",
        views.submit_assignment,
        name="submit_assignment",
    ),
]
