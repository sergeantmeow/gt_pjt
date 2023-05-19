from rest_framework import serializers
from .models import Movie, Cinema


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'vote_average', 'poster_path', 'id')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CinemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = 'name'  

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'