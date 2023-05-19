from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('search/', views.movie_search),
    path('<int:movie_pk>/', views.movie_detail),
    path('mbti/', views.movie_mbti),
]