from django.shortcuts import render, redirect
from .models import Article # models.py 안에 Article 연결
from .forms import ArticelForm # forms.py 안에 ArticleForm 연결



def index(request): # request: 클라이언트가 요청한 값
    return render(request, 'articles/index.html', {
        # DB에 저장된 객체를 변수에 저장해서 articles/index.html 파일로 랜더링 💡
        'articles': Article.objects.order_by('-pk'),
    })


def create(request):
    # 요청받은 메소드가 'POST'라면 요청 값을 저장
    if request.method == 'POST':
        article_form = ArticelForm(request.POST)
        # 요청한 값이 유효성 검사를 통과하면 값을 저장하고 인덱스 페이지로 이동
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    # 요청받은 메소드가 'GET'이라면 생성 페이지로 랜더링
    else:
        article_form = ArticelForm()
    return render(request, 'articles/create.html', {
        'article_form': article_form,
    })


def detail(request, pk):
    return render(request, 'articles/detail.html', {
        # DB에 저장된 특정한(pk값이 동일한) 객체를 변수에 저장해서 articles/detail.html 파일로 랜더링 💡
        'article': Article.objects.get(pk=pk),
    })


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청받은 메소드가 'POST'라면 요청 값을 저장, create와는 다르게 pk값을 Form의 instance로 저장
    if request.method == 'POST':
        article_form = ArticelForm(request.POST, instance=article)
        # 요청한 값이 유효성 검사를 통과하면 값을 저장하고 상세 페이지로 이동
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    # 요청받은 메소드가 'GET'이라면 수정 페이지로 랜더링
    else:
        article_form = ArticelForm(instance=article)
    return render(request, 'articles/update.html', {
        'article_form': article_form,
    })


def delete(request, pk):
    # 요청받은 pk값과 동일한 객체를 삭제하고,인덱스 페이지로 이동
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')