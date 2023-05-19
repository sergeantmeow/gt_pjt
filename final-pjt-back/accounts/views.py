from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # 사용자 모델에 mbti 필드가 있다면, 요청에서 해당 필드 값을 가져옵니다.
        mbti = serializer.validated_data.get('mbti', None)
        if mbti is not None:
            user.mbti = mbti
            user.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'key': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'mbti': user.mbti,
                'date_joined' : user.date_joined,
                'last_login' : user.last_login,
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class LogoutView(LogoutView):
    pass

class UserProfileView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            data = {
                'username': user.username,
                'mbti': user.mbti,
                'date_joined' : user.date_joined,
                'last_login' : user.last_login, 
            }
            return Response(data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)