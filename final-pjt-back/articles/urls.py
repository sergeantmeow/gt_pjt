from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('create/', views.article_create),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/like/', views.article_like),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/create', views.comment_create),
]
