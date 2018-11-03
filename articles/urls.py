from django.urls import path

from .views import (
    ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
)

urlpatterns = [
    path('articles/feed/', ArticlesFeedAPIView.as_view()),

    path('articles/<str:article_slug>)/favorite/',
        ArticlesFavoriteAPIView.as_view()),

    path('articles/<str:article_slug>)/comments/',
        CommentsListCreateAPIView.as_view()),

    path('articles/<str:article_slug>)/comments/<int:comment_pk>/',
        CommentsDestroyAPIView.as_view()),

    path('tags/', TagListAPIView.as_view()),
]
