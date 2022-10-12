from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model


class CustomUser(UserCreationForm):
    
    class meta:
        model = get_user_model()
        fields = ('username',),