from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200, null=True)
    genre_ids = models.ManyToManyField(Genre)
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

class Cinema(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    cood_x = models.FloatField(null=True)
    cood_y = models.FloatField(null=True)