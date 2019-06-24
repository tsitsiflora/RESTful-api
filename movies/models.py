from django.db import models
from datetime import datetime

# Create your models here.


class Movies(models.Model):
    title = models.CharField(max_length=50)
    released = models.DateField(default=datetime.now)
    runtime = models.IntegerField()
    description = models.TextField(max_length=300)
    ROMANCE = 'ROMANCE'
    COMEDY = 'COMEDY'
    THRILLER = 'THRILLER'
    SCIFI = 'SCI-FI'
    HORROR = 'HORROR'
    ADVENTURE = 'ADVENTURE'
    MYSTERY = 'MYSTERY'
    GENRE_CHOICES = [
        (ROMANCE, 'Romance'),
        (COMEDY, 'Comedy'),
        (THRILLER, 'Thriller'),
        (SCIFI, 'Sci-Fi'),
        (HORROR, 'Horror'),
        (ADVENTURE, 'Adventure'),
        (MYSTERY, 'Mystery'),

    ]
    genre = models.CharField(
        max_length=15,
        choices=GENRE_CHOICES,
        default=COMEDY,
    )
    director = models.ForeignKey(
        'Directors',
        on_delete=models.CASCADE,
    )
    main_actor = models.ForeignKey(
        'Actors',
        on_delete=models.CASCADE,
    )
    language = models.CharField(max_length=20)
    country = models.CharField(max_length=20)


class Directors(models.Model):
    name = models.CharField(max_length=20)
    movies_directed = models.ForeignKey('Movies', on_delete=models.CASCADE)
    country = models.CharField(max_length=20)


class Actors(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    movies_featured = models.ForeignKey('Movies', on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
