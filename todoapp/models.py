from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    tags = models.ForeignKey("Tag", on_delete=models.CASCADE)

    class Meta:
        ordering = ["completed", "-datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=255)
