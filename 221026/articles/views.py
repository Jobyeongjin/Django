from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.http import JsonResponse


def index(request):
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html',
    {
        'articles': articles,
    })

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
    form = CommentForm()
    return render(request, 'articles/detail.html',
    {
        'article': article,
        'comments': article.comments.all(),
        'form': form,
    })

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article:detail', pk)
        else:
            form = ArticleForm(instance=article)
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
    return render(request, 'articles/update.html',
    {
        'form': form,
    })

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
    return redirect('article:index')

def comment_create(request, pk):
    print(request.POST)
    article = Article.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    # return redirect('article:detail', article.pk)

        return JsonResponse({
            'content': comment.content,
            'comment_pk': comment.pk,
        })


def comment_delete(request, pk, comment_pk):
    print(request.POST)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    comment = False
    return JsonResponse(
        {
            'comment': comment,
            'comment_pk': comment_pk,
        }
    )
