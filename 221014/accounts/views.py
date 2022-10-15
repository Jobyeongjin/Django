from django.shortcuts import render, redirect
from .forms import CustomCreationForm, CustomChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model



def main(request):
    return render(request, 'accounts/main.html')


def signup(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('account:main')
    else:
        form = CustomCreationForm()
    return render(request, 'accounts/signup.html', 
    {
        'form': form, 
    })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'account:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',
    {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('account:main')


@login_required
def index(request):
    users = get_user_model().objects.all()
    return render(request, 'accounts/index.html',
    {
        'users': users,
    })


@login_required
def detail(request, pk):
    return render(request, 'accounts/detail.html')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:detail', request.user.pk)
    else:
        form = CustomChangeForm(instance=request.user)
    return render(request, 'accounts/update.html',
    {
        'form': form, 
    })


@login_required
def set_password(request):
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


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('account:main')