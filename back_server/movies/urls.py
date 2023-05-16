from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/search/', views.movie_search),
    path('movies/<int:movie_pk>/', views.movie_detail),
]