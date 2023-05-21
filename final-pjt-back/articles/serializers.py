from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user', 'username')


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'username', 'content', 'created_at', 'updated_at')
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    username = serializers.CharField(source='user.username', read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Article
        fields = ('id', 'username', 'like_users', 'title', 'content', 'image', 'created_at', 'updated_at', 'comments')
        read_only_fields = ('user', 'like_users')



