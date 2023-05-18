from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    mbti = serializers.CharField(max_length=4, required=False)  # mbti 필드 추가

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        super().get_cleaned_data()
        cleaned_data = {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'mbti': self.validated_data.get('mbti', ''),  # mbti 필드 추가
        }
        return cleaned_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        self.custom_signup(request, user)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)  # save 메서드 내에서 custom_signup 메서드를 다시 호출
        return user
