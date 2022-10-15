from email.policy import default
from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    gift_card = models.CharField(max_length=30)
    RATING = (
        (1, '⭐️'),
        (2, '⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️'),
        (5, '⭐️⭐️⭐️⭐️⭐️'),
    )
    grade = models.IntegerField(choices=RATING, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to='review_pics', default=None)
    image2 = models.ImageField(upload_to='review_pics', blank=True)
    image3 = models.ImageField(upload_to='review_pics', blank=True)
