from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create", views.create, name="create"),
    path(
        "toggle-todo-status/<int:todo_pk>",
        views.toggle_todo_status,
        name="toggle-todo-status",
    ),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
]
