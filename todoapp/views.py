from django.shortcuts import render
from django.views import generic

from todoapp.models import Task, Tag


def index(request):
    return render(request, "todoapp/index.html")


class TagListView(generic.ListView):
    model = Tag
