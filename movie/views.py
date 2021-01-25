from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Category, Actor, Genre
from .forms import ReviewsForm


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    """list films"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)

    # template_name = "movie/movie_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class MovieDetailView(GenreYear, DetailView):
    """film"""
    model = Movie
    # по какому полю нужно искаь запись
    slug_field = "url"


class AddReview(View):
    """отызвы"""

    def post(self, request, pk):
        # print(request.POST)
        form = ReviewsForm(request.POST)
        # print(form)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movie/actor.html'
    slug_field = "name"


class FilterMovieView(GenreYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset