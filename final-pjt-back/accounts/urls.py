from django.urls import path, include
from .views import CustomRegisterView, CustomLoginView, \
    LogoutView, UserProfileView, CustomUserDetailsView, \
    PasswordChangeView, user_follow, user_follower, user_following
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('signup/', CustomRegisterView.as_view(), name='rest_register'),
    path('edit/', CustomUserDetailsView.as_view(), name='rest_edit'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_pk>/', user_follow, name="follow" ),
    path('<int:user_pk>/followers', user_follower, name='user_follower'),
    path('<int:user_pk>/followings', user_following, name='user_following'),
]
