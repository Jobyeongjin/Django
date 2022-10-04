from django.shortcuts import render, redirect
from .models import Article # 현재 폴더의 models 연결
from .forms import ArticleForm # 현재 폴더의 forms의 ArticleForm 연결 


def index(request): # request: 클라이언트가 요청한 값
    articles = Article.objects.order_by('-pk') # DB에 저장된 객체를 변수에 저장 (pk를 기준으로 역순으로 정렬)
    # 리턴값 랜더링: articles 안에 index.html 파일로 저장한 변수값 전달
    return render(request, 'articles/index.html', {
        'articles': articles,
    })


def new(request):
    # 새로 만든 ArtcleForm 사용하여 템플릿(new.html)으로 전달 👍
    article_form = ArticleForm()
    # context라는 변수 설정 // 위에 articles와 동일한 작업 💡
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    # 만일 요청받은 메소드가 'POST'라면 요청 값을 저장
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        # 요청 값이 유효성 검사를 통과하면 저장하고 인덱스 페이지로 이동
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    # 요청받은 메소드가 'GET'이라면
    else:
        article_form = ArticleForm()
    # 유효성 검사를 통과하지 못하면 작성 페이지로 이동
    return render(request, 'articles/new.html', {
        'article_form': article_form,
    })


# 요청받은 값과 pk값을 인자로 사용 💡
def detail(request, pk):
    # pk값이 동일한 객체를 변수에 저장하고, detail 페이지로 랜더링
    article = Article.objects.get(pk=pk) 
    return render(request, 'articles/detail.html', {
        'article': article,
    })


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 만일 요청받은 메소드가 'POST'라면 요청 값을 저장
    if request.method == 'POST': 
        article_form = ArticleForm(request.POST, instance=article)
        # 유효성 검사를 통과하면 저장하고 디테일 페이지로 이동
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    # 요청받은 메소드가 'GET'이라면
    else:
        article_form = ArticleForm(instance=article)
    # 유효성 검사를 통과하지 못하면 다시 수정 페이지로 이동
    context = {
        'article': article,
        'article_form': article_form,
    }
    return render(request, 'articles/edit.html', context)


def delete(requset, pk):
    # 요청받은 pk값과 동일한 객체를 삭제하고, index 페이지로 이동
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')