# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, CinemaListSerializer
from .models import Movie, Cinema
import random

# Create your views here.
@api_view(['GET'])
def movie_search(request):
    pass


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    moviesList = []
    cnt = 1
    while cnt < 16:
        tmpMovie = movies[random.randrange(0, 998)]
        if tmpMovie not in moviesList:
            moviesList.append(tmpMovie)
            cnt += 1
    serializer = MovieListSerializer(moviesList, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_mbti(request):
    print('>>>>>reached view<<<<<<')
    movies = get_list_or_404(Movie)
    movieList = []
    userMbti = request.GET.get('mbti', '')
    mbtiMovie = {
        'INTJ': 9648, # mystery
        'INTP': 878, # SF
        'INFJ': 18, # drama
        'INFP': 14, # fantasy
        'ISTJ': 36, # history
        'ISTP': 80, # crime
        'ISFJ': 99, # documentary
        'ISFP': 16, # anime
        'ENTJ': 10752, # war
        'ENTP': 35, # comedy
        'ENFJ': 10749, # romance
        'ENFP': 12, # adventure
        'ESTJ': 53, # thriller
        'ESTP': 28, # action
        'ESFJ': 10749, # romance
        'ESFP': 10402, # music
    }
    userNum = mbtiMovie[userMbti]
    for i in movies:
        for j in i.genre_ids.all():
            if userNum == j.pk:
                movieList.append(i)
                break
    moviesList = []
    cnt = 1
    while cnt < 16:
        tmpMovie = movies[random.randrange(0, len(movieList)-1)]
        if tmpMovie not in moviesList:
            moviesList.append(tmpMovie)
            cnt += 1
    serializer = MovieListSerializer(moviesList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_cinema(request):
    userCoor = request.Get.get('coor', '')
    cinemas = get_list_or_404(Cinema)
    cinemaList = []
    for i in cinemas:
        if ((i.cood_x - userCoor[0]) ** 2 + (i.cood_y - userCoor[1]) ** 2) <= 10:
            cinemaList.append(i)
    serializer = CinemaListSerializer(cinemaList, many=True)
    return Response(serializer.data)