from django.urls import path, include
from .views import CustomRegisterView, CustomLoginView, LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('signup/', CustomRegisterView.as_view(), name='rest_register'),

]
