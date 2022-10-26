from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)