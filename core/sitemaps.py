from django.contrib.sitemaps import Sitemap

from movie_app.models import Movie,Genre


class GenreSitemap(Sitemap):
    def items(self):
        return Genre.objects.filter(is_active=True)

    def location(self, obj):
        return obj.get_absolute_url()
    

class MovieSitemap(Sitemap):
    def items(self):
        return Movie.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()  # `get_absolute_url` metodunuz olmalıdır.