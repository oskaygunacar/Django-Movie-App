from movie_app.models import Genre,Movie,Comments

# Python imports
import datetime

def processor(request):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    all_categories = Genre.objects.filter(is_active=True)
    latest_movies_processor = latest_movies = Movie.objects.order_by('-release_date').filter(is_active=True, release_date__range=("2004-01-01", today))[:20]
    latest_comments = Comments.objects.all()[:10]
    return {'categories':all_categories, 'latest_movies_processor':latest_movies_processor, 'latest_comments':latest_comments}