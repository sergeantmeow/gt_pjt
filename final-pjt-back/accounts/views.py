from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework import status, permissions
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import User

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

class MyProfileEditView(UserDetailsView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class UserProfileView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            followers = list(user.followers.values_list('username', flat=True))
            data = {
                'id' : user.id,
                'username': user.username,
                'mbti': user.mbti,
                'date_joined' : user.date_joined,
                'last_login' : user.last_login,
                'followers' : followers,
            }
            return Response(data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_follow(request, user_pk):
    if request.method == 'POST':
        user = request.user
        try:
            target_user = User.objects.get(pk=user_pk)
            if user != target_user:
                if target_user.followers.filter(pk=request.user.pk).exists():
                    target_user.followers.remove(request.user)
                else:
                    target_user.followers.add(request.user)
            return Response({'success': True, 'message': 'User followed successfully.'})
        except User.DoesNotExist:
            return Response({'success': False, 'message': 'User not found.'})
    else:
        return Response({'success': False, 'message': 'Invalid request method.'})