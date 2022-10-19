from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

from django.contrib.auth.decorators import login_required



def index(request):
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html',
    {
        'articles': articles,
    })


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
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
    return render(request, 'articles/detail.html',
    {
        'article': article,
    })


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
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
        Article.objects.get(pk=pk).delete()
        return redirect('article:index')
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()