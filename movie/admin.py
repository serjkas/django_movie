from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


# admin.site.register(Category, CategoryAdmin),
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    # пустые формы для отзывов а дминке, ограничение
    extra = 1
    readonly_fields = ("name", "email",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year", 'genres')

    # __name тк  нужно понять по какому полюю будем искать в модели категр
    search_fields = ("title", "category__name")
    # добавляем отзывы к фильму в дамине
    inlines = [ReviewInLine]
    # кнопки сохранения вверху
    save_on_top = True
    # соахранить с данными как нвоый
    save_as = True
    # list_editable = ("draft",)
    # fields = (("actors", "directors", "genres"),)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster")
        }),
        (None, {
            "fields": (("year", "word_premiere", "country"),)
        }),
        # 'classes': ('collapse',), сокрытие группы с Имененм Actors, И название их в начале
        ("Actors", {
            'classes': ('collapse',),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Optional", {
            "fields": (("url", "draft"),)
        })
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email",)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("name", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie")


admin.site.register(RatingStar)
