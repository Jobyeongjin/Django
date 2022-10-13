from django.shortcuts import render, redirect
# 커스텀한 폼 불러오기💡
from .forms import CustomCreationUser, CustomChangeUser
# 로그인 폼, 비밀번호 변경 폼💡
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# 커스텀하는 순간 커스텀한 유저를 가리킴💡
from django.contrib.auth import get_user_model
# 유저 정보를 세션에 저장 및 삭제하는 함수💡
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
# 로그인한 유저만 허용💡
from django.contrib.auth.decorators import login_required


"""메인페이지"""
def main(request):
    return render(request, 'accounts/main.html')


"""회원목록"""
@login_required
def index(request):
    users = get_user_model().objects.all()
    return render(request, 'accounts/index.html', 
    {
        'users': users,
    })


"""회원가입"""
def signup(request):
    # 회원가입 폼 사용하여 요청받은 정보를 입력하고, 검증한 뒤 저장하고 로그인💡
    if request.method == 'POST':
        form = CustomCreationUser(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('account:main')
    else:
        form = CustomCreationUser()
    return render(request, 'accounts/signup.html', 
    {
        'form': form,
    })


"""회원정보 상세보기"""
@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'accounts/detail.html',
    {
        'user': user,
    })


"""로그인"""
def login(request):
    # 로그인 폼을 사용하여 유저가 존재하는지 확인하고 요청한 데이터를 저장💡
    # -> 검증이 유효하다면 로그인💡
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'account:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', 
    {
        'form': form,
    })


"""로그아웃"""
@login_required
def logout(request):
    user_logout(request)
    return redirect('account:main')


"""회원정보 수정"""
@login_required
def update(request):
    # 👉 from .forms import CustomCreationUser, CustomChangeUser 👈
    # 회원수정 폼 사용해 요청받은 정보를 입력하고, 검증한 뒤 저장💡
    # -> 수정을 해야하니 유저 정보도 함께(instance) 넣기💡
    if request.method == 'POST':
        form = CustomChangeUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:main')
    else:
        form = CustomChangeUser(instance=request.user)
    return render(request, 'accounts/update.html', 
    {
        'form': form,
    })


"""비밀번호 수정"""
@login_required
def set_password(request):
    # 👉 from django.contrib.auth.forms import PasswordChangeForm 👈
    # django가 지원하는 패스워드 변경 폼💡
    # -> SetPasswordForm(이전 비밀번호 입력없이 변경) 클래스를 상속받음
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html', 
    {
        'form': form,
    })


"""회원탈퇴"""
@login_required
def delete(request):
    # 요청한 유저의 정보를 삭제한 뒤 로그아웃💡
    request.user.delete()
    user_logout(request)
    return redirect('account:main')