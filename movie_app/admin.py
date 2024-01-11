from django.contrib import admin
from .models import Movie, Genre,Profile

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', "release_date", 'movie_id']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "slug", "info"]