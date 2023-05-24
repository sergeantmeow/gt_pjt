from rest_framework import serializers
from .models import Movie, Cinema, Genre


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'vote_average', 'poster_path', 'id')

class MovieSerializer(serializers.ModelSerializer):
    genres_name = serializers.SerializerMethodField()
    def get_genres_name(self, movie):
        return [genre.name for genre in movie.genre_ids.all()]
    class Meta:
        model = Movie
        fields = '__all__'

class CinemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'  

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'
        