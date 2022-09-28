import re
from django.shortcuts import render, redirect
from .models import Post


def index(request):
    # 모든 글 목록 보여주기
    # 1. DB에서 모든 글을 불러오기
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    # 2. templates에 보내기
    return render(request, 'posts/index.html', context)


def new(request):
    return render(request, 'posts/new.html')

def create(request):
    # DB에 저장하는 로직
    # 1. parameter로 날라온 데이터를 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. DB에 저장
    Post.objects.create(title=title, content=content)

    context = {
        'title': title,
        'content': content,
    }

    # return render(request, 'posts/create.html', context)
    return redirect('posts:index')

def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')