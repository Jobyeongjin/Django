from django.db import models
# 👉이미지 처리하기: https://github.com/matthewwithanm/django-imagekit👈
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 사용전 Pillow 설치하기💡
    # -> pip install Pillow
    # 이미지 업로드에 사용하는 모델 필드💡
    # -> FileField를 상속받는 서브 클래스이기 때문에 모든 속성 및 메서드 사용 가능
    # -> upload_to: 업로드할 파일(MEDIA_ROOT)에 하위 경로 지정💡
    # -> blank: 빈 값 설정, 기본값 False💡
    image = models.ImageField(upload_to='images/', blank=True)
    # 썸네일 만들기💡
    thumbnail = ProcessedImageField(
        upload_to='images/',
        processors=[Thumbnail(100, 50)],
        format='JPEG',
        options={'quality': 80},
        blank=True,
        )
