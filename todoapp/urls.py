from django.urls import path

from todoapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("tag/", TagListView.as_view(), name="todo-list")
]

app_name = "todo"
