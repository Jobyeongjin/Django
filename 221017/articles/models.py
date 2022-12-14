from tkinter import CASCADE
from django.db import models
# ๐์ด๋ฏธ์ง ์ฒ๋ฆฌํ๊ธฐ: https://github.com/matthewwithanm/django-imagekit๐
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ์ฌ์ฉ์  Pillow ์ค์นํ๊ธฐ๐ก
    # -> pip install Pillow
    # ์ด๋ฏธ์ง ์๋ก๋์ ์ฌ์ฉํ๋ ๋ชจ๋ธ ํ๋๐ก
    # -> FileField๋ฅผ ์์๋ฐ๋ ์๋ธ ํด๋์ค์ด๊ธฐ ๋๋ฌธ์ ๋ชจ๋  ์์ฑ ๋ฐ ๋ฉ์๋ ์ฌ์ฉ ๊ฐ๋ฅ
    # -> upload_to: ์๋ก๋ํ  ํ์ผ(MEDIA_ROOT)์ ํ์ ๊ฒฝ๋ก ์ง์ ๐ก
    # -> blank: ๋น ๊ฐ ์ค์ , ๊ธฐ๋ณธ๊ฐ False๐ก
    image = models.ImageField(upload_to='images/', blank=True)
    # ์ธ๋ค์ผ ๋ง๋ค๊ธฐ๐ก
    thumbnail = ProcessedImageField(
        upload_to='images/',
        processors=[Thumbnail(100, 50)],
        format='JPEG',
        options={'quality': 80},
        blank=True,
        )

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)