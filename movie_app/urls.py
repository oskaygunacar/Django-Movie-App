from django.contrib import admin
from django.urls import path

# views
from . import views

app_name = "movie_app"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("movie/<slug:movie_slug>/", views.movie_detail_view, name="movie_detail_view"),
    path("category/<slug:category_slug>/", views.category_view, name="category_detail_view"),
    path("most-popular-movies/", views.most_popular_movies_view, name="most_popular_movies"),
    path('account/delete-account/', views.delete_account_view, name="delete_account_view"),
    path('account/change-password/', views.change_password_view, name='change_password'),
    path('account/update-profile/', views.update_profile_view, name="update_profile_view" ),
    path('account/<slug:profile_slug>/', views.profile_detail_view, name='profile_detail_view'),
    path('login/', views.login_view, name="login"),
    path("signup/", views.signup_View, name='signup'),
    path('logout/', views.logout_view, name="logout"),
    path('s', views.search, name="search"),
]
