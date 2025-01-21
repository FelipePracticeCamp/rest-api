from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(null=True, blank=True, validators=(
        MaxValueValidator(5, 'O máximo de estrelas é 5'), 
        MinValueValidator(0, 'O mnínimo de estrelas é 0')))
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
