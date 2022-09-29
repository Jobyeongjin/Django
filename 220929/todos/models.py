from datetime import date
from email.policy import default
from venv import create
from django.db import models



class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
