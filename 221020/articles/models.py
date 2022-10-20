from django.db import models
from django.conf import settings



class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comments', on_delete=models.CASCADE)
    article = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='article_comments', on_delete=models.CASCADE)
