from django.db import models
# from accounts.models import User
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    
