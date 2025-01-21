from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer, MovieModelSerializer
from rest_framework.views import APIView
from django.db.models import Count, Avg
from reviews.models import Review
from rest_framework import response
from rest_framework.status import HTTP_200_OK


# Create your views here.
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieModelSerializer
        else:
            return MovieSerializer




class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(APIView):
    queryset = Movie.objects.all()

    def get(self):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(
            stars_avg = Avg('stars')
        )['stars_avg']

        return response.Response(
            data={
                "total_movies":total_movies,
                "movies_by_genre":movies_by_genre,
                "total_reviewws":total_reviews,
                "average_stars":average_stars,
                },
            status=HTTP_200_OK
        )