from django.shortcuts import render, redirect
from articles.forms import ArticleForm
from .models import Article



def index(request):
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html',
    {
        'articles': articles,
    })


def create(request):
    if request.method == 'POST':
        # request.FILES: 템플릿 폼에서 요청받은 업로드 파일 객체로 확인💡
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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


def update(request, pk):
    article = Article.objects.get(pk=pk)
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


def delete(request, pk):
    article = Article.objects.get(pk=pk).delete()
    return redirect('article:index')
