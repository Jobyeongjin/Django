from django.shortcuts import render
from day0926.settings import BASE_DIR
from .models import Article

guestbook = []

def index(request):

    guestbook = Article.objects.all()

    return render(request, 'articles/index.html', {
        'guestbook': guestbook,
    })

def create(request):

    content = request.GET.get('content')
    guestbook.append(content)
    Article.objects.create(content=content)

    return render(request, 'articles/create.html', {
        'content': content,
    })