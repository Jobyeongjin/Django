from django.shortcuts import render, redirect
from .forms import CustomUser
from .models import User


def main(request):
    return render(request, 'accounts/main.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:index')
    else:
        form = CustomUser()
    return render(request, 'accounts/signup.html', 
    {
        'form': form,
    })


def index(request):
    users = User.objects.all()

    return render(request, 'accounts/index.html',
    {
        'users': users,
    })


def detail(request, pk):
    return render(request, 'accounts/detail.html')