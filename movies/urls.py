from django.urls import path
from .views import MoviesView, DeleteMovie

urlpatterns = [
    path('movies', MoviesView.as_view(), name='movies'),
    path('deletemovie', DeleteMovie.as_view(), name='delete_movie'),
]
