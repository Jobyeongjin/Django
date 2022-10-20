from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
from .models import Article, Comment


def index(request):
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html',
    {
        'articles': articles,
    })


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('article:index')
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html',
    {
        'form': form,
    })


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    return render(request, 'articles/detail.html',
    {
        'article': article,
        'form': form,
        'comments': article.comments.order_by('-pk'),
    })


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        return render(request, 'articles/update.html',
        {
            'form': form,
        })
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
    return redirect('article:index')


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        user = request.user
        comment.user = user
        comment.article = article
        comment.save()
    return redirect('article:detail', article.pk)


@login_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
    return redirect('article:detail', pk)
