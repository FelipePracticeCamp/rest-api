from rest_framework import serializers
from .models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Movie
        fields = '__all__'

    
    
    def validade_resume(self, value):
        if len(value) > 800:
            raise serializers.ValidationError('O máximo de caracteres permitido é de 800')
        else:
            return value



class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(
            stars_avg=Avg('stars')
        )['stars_avg']

        if not rate:
            return None
        else:
            return rate