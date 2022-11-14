from django.urls import path

from todoapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/update_status/<int:pk>/", task_status_update, name="task-update-status")
]

app_name = "todo"
