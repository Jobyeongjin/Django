from django.shortcuts import render, redirect
from .forms import CustomCreationUser, CustomChangeUser
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'users/main.html')


@login_required
def index(request):
    users = get_user_model().objects.all()
    return render(request, 'users/index.html', 
    {
        'users': users,
    })


def signup(request):
    if request.method == 'POST':
        form = CustomCreationUser(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('user:main')
    else:
        form = CustomCreationUser()
    return render(request, 'users/signup.html',  
    {
        'form': form, 
    })

@login_required
def detail(request, pk):
    return render(request, 'users/detail.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'user:main')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', 
    {
        'form': form,
    })

@login_required
def logout(request):
    user_logout(request)
    return redirect('user:main')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomChangeUser(request.POSt, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:main')
    else:
        form = CustomChangeUser(instance=request.user)
    return render(request, 'users/update.html',
    {
        'form': form,
    })

@login_required
def set_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password.html', 
    {
        'form': form, 
    })

@login_required
def delete(request):
    request.user.delete()
    user_logout(request)
    return redirect('user:main')