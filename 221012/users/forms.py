# django에서 지원하는 회원가입 폼💡
# -> 비밀번호 등 검증을 도와줌💡
from django.contrib.auth.forms import UserCreationForm
# user model을 가리키는 함수💡
# -> 커스텀하는 순간 커스텀한 User model을 가리킴💡
from django.contrib.auth import get_user_model


# 상속 받아 커스터마이징💡
class CustomUser(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )