from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html',
    {
        'form': form,
    })


def index(request):
    reviews = Review.objects.order_by('-pk')
    return render(request, 'reviews/index.html',
    {
        'reviews': reviews, 
    })


@login_required
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'reviews/detail.html',
    {
        'review': review,
    })


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/update.html',
    {
        'form': form, 
    })


@login_required
def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('review:index')