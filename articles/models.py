import uuid

from django.db import models

from model_utils.models import TimeStampedModel


class Article(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    author = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='articles'
    )

    tags = models.ManyToManyField(
        'articles.Tag', related_name='articles', null=True
    )

    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='articles',
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created', '-modified']


class Comment(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'profiles.Profile', related_name='comments', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created', '-modified']


class Tag(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    tag = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created', '-modified']

    def __str__(self):
        return self.tag
