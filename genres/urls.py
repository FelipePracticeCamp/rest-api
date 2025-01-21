
from django.urls import path
from .views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path("genres_list/", GenreListCreateView.as_view(), name='genres_list'),
    path("genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name='genre_retrieve')
]
