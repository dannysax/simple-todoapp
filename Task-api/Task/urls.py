from django.urls import path
from . import views

urlpatterns = [
    path("", views.url_overview, name="urls"),
    path("task-list/", views.task_list, name="task-list"),
    path("task-detail/<str:pk>", views.task_detail, name="task-detail"),
    path("task-create", views.task_create, name="task-create"),
    path("task-edit/<str:pk>", views.task_edit, name="task-edit"),
    path("task-delete/<str:pk>", views.task_delete, name="task-delete")
    ]