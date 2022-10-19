from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm




def main(request):
    return render(request, 'accounts/main.html')


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


@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:main')


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


@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'accounts/detail.html',
    {
        'user': user,
        'articles': user.articles.all(),
    })