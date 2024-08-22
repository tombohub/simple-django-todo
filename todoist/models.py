from django.db import models


# Create your models here.
class Todo(models.Model):
    class Status(models.TextChoices):
        DONE = "Done", "Done"
        NOT_DONE = "Not Done", "Not Done"

    title = models.CharField(max_length=20)
    status = models.TextField(choices=Status.choices, default=Status.NOT_DONE)
