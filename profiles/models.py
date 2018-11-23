import uuid

from model_utils.models import TimeStampedModel

from django.db import models


class Profile(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        'users.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)

    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )

    favorites = models.ManyToManyField(
        'articles.Article',
        related_name='favorited_by'
    )

    follows_tag = models.ManyToManyField(
        'articles.Tag',
        related_name='followed_by',
        symmetrical=False
    )

    def __str__(self):
        return self.user.username

    # Follow user
    def follow(self, profile):
        self.follows.add(profile)

    def unfollow(self, profile):
        self.follows.remove(profile)

    def is_following(self, profile):
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        return self.followed_by.filter(pk=profile.pk).exists()

    # Favorite article
    def favorite(self, article):
        self.favorites.add(article)

    def unfavorite(self, article):
        self.favorites.remove(article)

    def has_favorited(self, article):
        return self.favorites.filter(pk=article.pk).exists()

    # Tag
    def follow_tag(self, profile):
        self.follows_tag.add(profile)

    def unfollow_tag(self, profile):
        self.follows_tag.remove(profile)

    def is_following_tag(self, profile):
        return self.follows_tag.exists()
