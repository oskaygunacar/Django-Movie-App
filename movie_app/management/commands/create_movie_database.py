from django.core.management.base import BaseCommand
from movie_app.models import Movie,Genre
import requests
import threading
import time

class Command(BaseCommand):
    help = 'create a movie database which contains appr. 10000 movie from https://www.themoviedb.org/ API'

    api_read_token = "" # write your api read token here.

    api_key = "" # write your api key here.

    def get_all_genres(self):
        url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}'
        genres_response = requests.get(url)
        return [i['name'] for i in genres_response.json().get('genres')]
    
    def create_genres(self):
        genre_list = self.get_all_genres()
        for genre in genre_list:
            obj, created = Genre.objects.get_or_create(title=genre)

    def get_video(self, movie_id):
        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {self.api_read_token}"
        }
        video_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/videos', headers=headers)
        print(movie_id)
        if video_response.json().get('results') != []:
            video_key = video_response.json().get('results')[0].get('key') 
            video = f'https://www.youtube.com/embed/{video_key}'
            return video
        return "#"


    def get_movie_genres(self,movie_genres):
        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {self.api_read_token}"
        }
        url = f'https://api.themoviedb.org/3/genre/movie/list'
        genres_response = requests.get(url, headers=headers)
        genre_names = [genre['name'] for genre in genres_response.json().get('genres') if genre['id'] in movie_genres] # comprehension
        return genre_names
    
    def get_all_videos(self,start_page,end_page):
        self.create_genres()
        print(f"Thread {threading.current_thread().name}")
        for page in range(start_page,end_page):
            print("PAGE:", page)
            url = f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&include_adult=false&language=en-US&page={page}&sort_by=release_date.desc'
            
            response = requests.get(url)
            for movie_data in response.json().get('results'):
                try:
                    movie_id = movie_data.get('id')
                    title = movie_data.get('title')
                    overview = movie_data.get('overview')
                    poster = f"https://image.tmdb.org/t/p/original/{movie_data.get('poster_path','#')}"
                    language = movie_data.get('original_language', 'en')
                    vote_average = movie_data.get('vote_average', '0')
                    release_date = movie_data.get('release_date', '2000-01-01')
                    popularity = movie_data.get('popularity', '0.0')
                    genres = self.get_movie_genres(movie_data.get('genre_ids', ''))
                    video = self.get_video(movie_id=movie_id)
                    movie, created = Movie.objects.get_or_create(movie_id=movie_id, title=title, defaults={
                        'overview': overview,
                        'poster': poster,
                        'language': language,
                        'vote_average': vote_average,
                        'release_date': release_date,
                        'popularity': popularity,
                        'video': video,
                    })
                    if created:       
                            for genre_name in genres:
                                genre_obj, _ = Genre.objects.get_or_create(title=genre_name)
                                movie.genre.add(genre_obj)
                            print(f"{movie.title} succesfully created.")
                    else:
                        movie.overview = overview
                        movie.poster = poster
                        movie.language = language
                        movie.vote_average = vote_average
                        movie.release_date = release_date
                        movie.popularity = popularity
                        movie.video = video
                        movie.save()
                        print(f'{movie.title} already exist. Movie fields updated according to new data.')

                except Exception as e:
                    print(f"Error creating movie {movie_id}: {e}")
                


    def handle(self, *args, **kwargs):
        total_pages = 500
        threads_per_batch = 13

        for j in range(39):  # 39 * 13 -> 507 pages in total
            threads = list()
            for i in range(threads_per_batch):
                page = j * threads_per_batch + i + 1
                if page <= total_pages:
                    thread = threading.Thread(target=self.get_all_videos, args=(page, page + 1))
                    threads.append(thread)
                    thread.start()
            
            for thread in threads:
                thread.join()
            
            time.sleep(10)

