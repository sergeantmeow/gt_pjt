from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer, UserSerializer, CustomUserDetailsSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

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

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer

    def update(self, request, *args, **kwargs):
        partial = True # 부분 업데이트를 허용
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # 추가적으로 업데이트할 필드
        instance.mbti = serializer.validated_data.get('mbti', instance.mbti)
        
        # 업데이트할 것들 저장
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class CustomPasswordChangeView(PasswordChangeView):
    pass

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
    if request.method == 'GET':
        user = request.user
        try:
            target_user = User.objects.get(pk=user_pk)
            followers = target_user.followers.all()
            serializer = UserSerializer(followers, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'success': False, 'message': 'User not found.'})
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_follower(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    followers = user.followers.all()

    follower_list = []
    for follower in followers:
        follower_list.append({
            'id': follower.id,
            'username': follower.username,
            # Include other fields you want to return
        })

    return Response(follower_list)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_following(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    following = user.followings.all()

    following_list = []
    for followed_user in following:
        following_list.append({
            'id': followed_user.id,
            'username': followed_user.username,
            'email': followed_user.email,
            # Include other fields you want to return
        })

    return Response(following_list)