from django import forms

from todoapp.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(widget=forms.DateTimeInput)

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
