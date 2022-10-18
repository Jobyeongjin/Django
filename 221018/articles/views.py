from django.shortcuts import render, redirect
from articles.forms import ArticleForm, CommentForm
from .models import Article, Comment



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
    # 댓글 폼 보여주기💡
    form = CommentForm()
    return render(request, 'articles/detail.html',
    {
        'article': article,
        # 게시글의 모든 댓글(역참조)💡
        # -> comment_set을 사용하지 않고, related_name을 사용해 comments로 변경💡
        'comments': article.comments.all(),
        'form': form,
    })


def update(request, pk):
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


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('article:index')



# 댓글 생성 로직💡
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # DB에 바로 저장하지 않음💡
        # -> NOT NULL constraint falied: ..._id 
        # --> 댓글 모델 생성 이전에 이미 생성된 게시글에 id값이 누락되있기 때문💡
        # -> id값을 찾아서 넣어주고 저장
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('article:detail', article.pk)


def comment_update(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('article:detail', pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'articles/update_com.html', {
        'form': form,
    })
    


# 댓글 삭제 로직💡
def comment_delete(request, pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('article:detail', pk)