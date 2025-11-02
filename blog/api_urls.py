from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ArticleApi, CommentApi

router = DefaultRouter()
router.register(r'articles', ArticleApi)
router.register(r'comment', CommentApi)

urlpatterns = [
    path('', include(router.urls)),
]