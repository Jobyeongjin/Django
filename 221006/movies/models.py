from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField()
    running_time = models.PositiveIntegerField()

    def __str__(self):
        return self.title
