# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, CinemaListSerializer, GenreSerializer
from .models import Movie, Cinema, Genre
import random
from .kakaoLocalAPI import KakaoLocalAPI

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
    
    # create kakaolocalapi instance
    rest_api_key = '76752d0d9176755783a651b7f2ea1ce5'
    kakao = KakaoLocalAPI(rest_api_key)
    input_coord = 'WGS84'
    output_coord = 'TM'

    # get user coordinates
    co_y = float(request.GET.get('co_x', ''))
    co_x = float(request.GET.get('co_y', ''))

    convertedResult = kakao.geo_transcoord(co_x, co_y, output_coord)
    userX = convertedResult['documents'][0]['x']
    userY = convertedResult['documents'][0]['y']

    cinemas = get_list_or_404(Cinema)
    cinemaList = []
    for i in cinemas:
        if i.cood_x != None:
            if ((float(i.cood_x) - userX) ** 2 + (float(i.cood_y) - userY) ** 2) ** (1/2) <= 4500: # edit this number to adjust the search range
                cinemaList.append(i)
    serializer = CinemaListSerializer(cinemaList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_high(request):
    movies = get_list_or_404(Movie.objects.filter(vote_average__gte=8.2))
    moviesList = []
    cnt = 1
    while cnt < 16:
        tmpMovie = movies[random.randrange(0, len(movies)-1)]
        if tmpMovie not in moviesList:
            moviesList.append(tmpMovie)
            cnt += 1
    serializer = MovieListSerializer(moviesList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_retro(request):
    movies = get_list_or_404(Movie.objects.filter(release_date__contains="199"))
    moviesList = []
    cnt = 1
    while cnt < 16:
        tmpMovie = movies[random.randrange(0, len(movies)-1)]
        if tmpMovie not in moviesList:
            moviesList.append(tmpMovie)
            cnt += 1
    serializer = MovieListSerializer(moviesList, many=True)
    return Response(serializer.data)
