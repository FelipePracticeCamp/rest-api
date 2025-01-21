from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView, MovieStatsView


urlpatterns = [
    path("movies_list/", MovieListCreateView.as_view(), name='movies_list'),
    path("movies/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name='movies_retrieve'),
    path("stats/", MovieStatsView.as_view(), name='stats'),
]
