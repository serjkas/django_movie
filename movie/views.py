from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewsForm


class MoviesView(ListView):
    """list films"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movie/movie_list.html"


class MovieDetailView(DetailView):
    """film"""
    model = Movie
    # по какому полю нужно искаь запись
    slug_field = "url"


class AddReview(View):
    """отызвы"""
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie_id = pk
            form.save()
        return redirect("/")