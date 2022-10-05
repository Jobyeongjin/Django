from django.db import models


# DB 모델 설계하기 💡
class Article(models.Model):
    title = models.CharField(max_length=30) # 문자열 필드, 글자수 제한: 30
    content = models.TextField() # 텍스트 필드
    created_at = models.DateTimeField(auto_now_add=True) # 날짜시간 필드, 생성시 시간으로 설정
    updated_at = models.DateTimeField(auto_now=True) # 날짜시간 필드, 수정시 시간으로 업데이트

# 설계 이후 python3 manage.py makemigrations && python3 manage.py migrate 실행 💡