from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todoapp.models import Task, Tag


def index(request):
    return render(request, "todoapp/index.html")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
