# from .models import User
# User model을 커스텀하고 부르는 함수💡
# -> 이 함수는 기본적으로는 User를 보고 있지만, 커스텀 하는 순간 커스텀한 User model을 가리킴💡
# -> User는 언제든 바뀔 수 있기 때문에 직접 model에서 부르지 않는 것💡
# -> 따라서 맨위 코드는 쓸 일이 없음!!!
from django.contrib.auth import get_user_model


# django에서 이미 만들어놓은 회원가입을 위한 폼(비밀번호 등 인증/검증을 도와줌!!!)을 가져다가 쓰기💡
from django.contrib.auth.forms import UserCreationForm


# 상속을 받아서 커스텀마이징💡
class CustomUser(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
    