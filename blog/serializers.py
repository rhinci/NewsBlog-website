from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Comment
        fields = '__all__'


