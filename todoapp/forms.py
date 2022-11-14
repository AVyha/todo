from django import forms

from todoapp.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
