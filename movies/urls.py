from django.urls import path
from .views import MovieView, MovieDetailView, OrderDetailView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", OrderDetailView.as_view())
]