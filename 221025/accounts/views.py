from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.http import JsonResponse


def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
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
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',
    {
        'form': form,
    })

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'accounts/detail.html',
    {
        'user': user,
    })

"""Follow"""
def follow(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if user != request.user:
        if user.followings.filter(pk=request.user.pk).exists():
            user.followings.remove(request.user)
            is_followed = False
        else:
            user.followings.add(request.user)
            is_followed = True
        return JsonResponse(
            {
                'is_followed': is_followed,
                'followers_count': user.followers.count(),
                'followings_count': user.followings.count(),
            }
        )
    return redirect('accounts:detail', pk)