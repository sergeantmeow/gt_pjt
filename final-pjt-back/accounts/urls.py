from django.urls import path, include
from .views import CustomRegisterView, CustomLoginView, LogoutView, UserProfileView, MyProfileEditView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('signup/', CustomRegisterView.as_view(), name='rest_register'),
    path('edit/<str:username>/', MyProfileEditView.as_view(), name='rest_edit'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_pk>/', views.user_follow, name="follow" )
]
