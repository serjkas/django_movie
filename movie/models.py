from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=150)
    description = models.TextField(verbose_name="Описание")
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", default=0)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер \ Режисер"
        verbose_name_plural = "Актеры \ Режисеры"


class Genre(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    tagline = models.CharField(verbose_name="Слоган", max_length=100, default='')
    description = models.TextField(verbose_name="Описане")
    poster = models.ImageField(verbose_name='Постер', upload_to="movies/")
    year = models.PositiveSmallIntegerField(verbose_name='Дата выхода', default="2020")
    country = models.CharField(verbose_name="Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Дректор", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    word_premiere = models.DateField(verbose_name="Мированя примьера", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="сумма в долларах")
    fees_in_usa = models.PositiveIntegerField("Сброы в США", default=0, help_text="сумма в долларах")
    fees_in_world = models.PositiveIntegerField("Сброы в мире", default=0, help_text="сумма в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    description = models.TextField(verbose_name="Описане")
    image = models.ImageField(verbose_name='Изображение', upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильм"
        verbose_name_plural = "Кадры из фильмов"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, related_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    # 'self' ссылается на саму себя в таблице
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )

    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
