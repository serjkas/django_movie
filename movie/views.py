from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


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


