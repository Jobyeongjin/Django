from django.contrib.auth.models import AbstractUser

# django에서 지원하는 로그인 모델💡
# -> 암호화 및 검증을 도움💡
class User(AbstractUser):
    
    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'