# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

# Create your views here.
@api_view(['GET'])
def movie_search(request):
    pass


@api_view(['GET'])
def movie_detail():
    pass


def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)