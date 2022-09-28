from email.policy import default
from xmlrpc.client import Boolean
from django.db import models



class Todo(models.Model):
    # django에서는 pk(id)를 자동으로 생성합니다.
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    