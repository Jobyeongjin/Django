from django.shortcuts import render, redirect
from .models import MovieInfo, Review
from .forms import ReviewForm



def main(request):
    movie_info = MovieInfo.objects.all()
    review_len = len([*Review.objects.all()])

    return render(request, 'reviews/main.html', 
    {
        'movie_info': movie_info,
        'review_len': review_len,
    })


def index(request):
    reviews = Review.objects.order_by('-pk')
    review_len = len([*Review.objects.all()])

    return render(request, 'reviews/index.html', 
    {
        'reviews': reviews,
        'review_len': review_len,
    })


def search(request):
    review_title = request.GET.get('review-title')
    review_len = len([*Review.objects.all()])
    retrieved_review_data = Review.objects.filter(title__icontains=review_title)
    
    return render(request, 'reviews/index.html', 
    {
        'retrieved_review_data': retrieved_review_data,
        'review_len': review_len,
    })


def create(request, pk):
    movie_info = MovieInfo.objects.get(pk=pk)
    review_len = len([*Review.objects.all()])

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        grade = int(request.POST.get('review_grade'))
        if review_form.is_valid():
            review_form.save()
            review = Review.objects.order_by('-pk')[0]
            review.movie_pk = movie_info.pk
            review.save()
            movie_info.movie_grade += grade
            movie_info.movie_avg = movie_info.movie_grade / movie_info.vote
            movie_info.save()
            return redirect('review:index')
    else:
        review_form = ReviewForm()

    return render(request, 'reviews/create.html', 
    {
        'review_form': review_form,
        'movie_title': movie_info.movie_name,
        'review_len': review_len,
    })


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    review_len = len([*Review.objects.all()])

    return render(request, 'reviews/detail.html', 
    {
        'review': review,
        'review_len': review_len,
    })


def update(request, pk):
    review = Review.objects.get(pk=pk)
    review_len = len([*Review.objects.all()])
    old_grade = review.review_grade

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            review = Review.objects.get(pk=pk)
            new_grade = review.review_grade
            if old_grade != new_grade:
                movie_pk = review.movie_pk
                movie_info = MovieInfo.objects.get(pk=movie_pk)
                movie_info.movie_grade -= old_grade
                movie_info.movie_grade += new_grade
                movie_info.movie_avg = movie_info.movie_grade / movie_info.vote
                movie_info.save()
            else:
                pass
            return redirect('review:detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'reviews/update.html', 
    {
        'review': review,
        'review_form': review_form,
        'review_len': review_len,
    })


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    grade = review.review_grade
    movie_pk = review.movie_pk
    movie_info = MovieInfo.objects.get(pk=movie_pk)
    movie_info.movie_grade -= grade
    movie_info.vote -= 1
    
    if movie_info.vote:
        movie_info.movie_avg = movie_info.movie_grade / movie_info.vote
    else:
        movie_info.movie_avg = 0
    movie_info.save()
    review.delete()

    return redirect('review:index')