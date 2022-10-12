from django.shortcuts import render, redirect
# 커스텀한 유저 폼💡
from .forms import CustomUser
# user model을 가리키는 함수💡
# -> 커스텀하는 순간 커스텀한 User model을 가리킴💡
from django.contrib.auth import get_user_model
# django가 지원하는 로그인 폼으로 유저가 존재하는지 검증함💡
from django.contrib.auth.forms import AuthenticationForm
# 유저 정보를 세션에 저장하는 함수💡
from django.contrib.auth import login as user_login
# 세션에 담겨있는 유저 정보를 삭제하는 함수💡
from django.contrib.auth import logout as user_logout
# 로그인한 유저만 허용하기💡
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'users/main.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        # 유효성 검사 후 폼 데이터를 변수에 저장해 세션에 담기💡
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('user:index')
    else:
        form = CustomUser()
    return render(request, 'users/signup.html', 
    {
        'form': form,
    })


# 👉 from django.contrib.auth.decorators import login_required 👈
# -> 로그인 유저만 허용하는 @데코레이터 / 함수에만 사용 가능💡
@login_required
def index(request):
    users = get_user_model().objects.all()
    return render(request, 'users/index.html',
    {
        'users': users,
    })


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'users/detail.html', 
    {
        'user': user,
    })


def login(request):
    if request.method == 'POST':
        # 👉 from django.contrib.auth.forms import AuthenticationForm 👈
        # django에서 지원하는 로그인 폼💡
        # -> modelForm이랑 혼돈하지 말자!!!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 👉 from django.contrib.auth import login as user_login 👈
            # login 함수는 request, user를 인자로 받음, 세션에 아이디를 저장💡
            # -> 정의하는 함수와 이름이 같아 네임 변경💡
            user_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'user:main')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html',
    {
        'form': form,
    })


def logout(request):
    # 세션 삭제💡
    user_logout(request)
    return redirect ('user:main')