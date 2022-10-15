from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class CustomChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )