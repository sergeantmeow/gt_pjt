from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('search/', views.movie_search),
    path('<int:movie_pk>/', views.movie_detail),
    path('mbti/', views.movie_mbti),
    path('cinema/', views.movie_cinema),
    path('high/', views.movie_high),
    path('retro/', views.movie_retro),
]