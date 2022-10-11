# from django.db import models
# django 내부에서 지원(로그인 모델)하는 user를 가져다가 씀💡
# -> 이 클래스를 사용함으로써 간단하게 암호화 및 인증을 할 수가 있다!!!
# -> 따라서(이미 참조하고 있기에) 맨위 코드는 쓸 일이 없음!!!
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass