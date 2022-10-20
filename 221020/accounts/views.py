from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm



def main(request):
    return render(request, 'accounts/main.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html',
    {
        'form': form,
    })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',
    {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('accounts:main')


def detail(request, pk):
    return render(request, 'accounts/detail.html')


def update(request, pk):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html',
    {
        'form': form,
    })


def delete(request, pk):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:main')


def set_password(request, pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html',
    {
        'form': form,
    })