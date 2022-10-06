from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


def index(request):
    return render(
        request,
        "movies/index.html",
        {
            "movies": Movie.objects.order_by("-pk"),
        },
    )


def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movies:index")
    else:
        movie_form = MovieForm()
    return render(
        request,
        "movies/create.html",
        {
            "movie_form": movie_form,
        },
    )


def detail(request, pk):
    return render(
        request,
        "movies/detail.html",
        {
            "movie": Movie.objects.get(pk=pk),
        },
    )


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movies:detail", movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    return render(
        request,
        "movies/update.html",
        {
            "movie_form": movie_form,
        },
    )


def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect("movies:index")
