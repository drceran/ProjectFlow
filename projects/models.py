from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    # tasks=[Task, Task, Task]
    def __str__(self):
        return self.name
