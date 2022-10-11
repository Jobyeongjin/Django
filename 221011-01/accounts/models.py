from django.db import models
# django 내부에서 지원하는 user를 가져다가 씀💡
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
