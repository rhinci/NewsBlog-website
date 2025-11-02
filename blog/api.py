from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

class ArticleApi(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentApi(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer