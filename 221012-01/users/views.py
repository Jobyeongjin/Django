from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
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
        form = CustomUser(request.POST)
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


@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'users/detail.html', 
    {
        'user': user,
    })


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


def logout(request):
    user_logout(request)
    return redirect('user:main')