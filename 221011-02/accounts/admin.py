from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# User model을 커스텀하고 부르는 함수💡
# -> 이 함수는 기본적으로는 User를 보고 있지만, 커스텀 하는 순간 커스텀한 User model을 가리킴💡
# -> User는 언제든 바뀔 수 있기 때문에 직접 model에서 부르지 않는 것💡
# -> 따라서 아래 코드는 쓸 일이 없음!!!
# from .models import User 
from django.contrib.auth import get_user_model



admin.site.register(get_user_model(), UserAdmin)