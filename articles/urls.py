from django.urls import path

from .views import (
    ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView,
    TagFollowAPIView
)

urlpatterns = [
    path('articles/feed/', ArticlesFeedAPIView.as_view()),

    path('articles/<slug:article_slug>/favorite/',
        ArticlesFavoriteAPIView.as_view()),

    path('articles/<slug:article_slug>/comments/',
        CommentsListCreateAPIView.as_view()),

    path('articles/<slug:article_slug>/comments/<int:comment_pk>/',
        CommentsDestroyAPIView.as_view()),

    path('tags/', TagListAPIView.as_view()),
    path('tags/<str:tag>/follow/', TagFollowAPIView.as_view()),
]
