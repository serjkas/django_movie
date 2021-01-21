from django import template

from movie.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """вывод каткгорий"""
    return Category.objects.all()


@register.inclusion_tag('movie/tags/last_movies.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}
