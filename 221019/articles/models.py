from django.db import models
# from accounts.models import User
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
    

class Comment(models.Model):
    content = models.CharField(max_length=50)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)