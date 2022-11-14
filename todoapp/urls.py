from django.urls import path

from todoapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
