# django가 지원하는 로그인 모델💡
# -> 이 클래스를 사용함으로써 암호화 및 인증을 할 수 있음💡
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
