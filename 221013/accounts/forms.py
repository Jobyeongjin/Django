from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


# django가 지원하는 회원가입 폼을 상속받아 커스텀💡
class CustomCreationUser(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2',
        )


# django가 지원하는 회원수정 폼을 상속받아 커스텀💡
class CustomChangeUser(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
        )