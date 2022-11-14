from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from todoapp.forms import TaskForm
from todoapp.models import Task, Tag


def index(request):
    context = {
        "completed_task": Task.objects.filter(completed=True).count(),
        "uncompleted_task": Task.objects.filter(completed=False).count()
    }
    return render(request, "todoapp/index.html", context)


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


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


def task_status_update(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))
