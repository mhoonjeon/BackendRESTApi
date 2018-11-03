import pytz
import factory

from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_

from core.utils import to_dict
from .factories import ArticleFactory, CommentFactory, TagFactory
from ..models import Tag
from ..serializers import (
    ArticleSerializer, CommentSerializer, TagSerializer
)
from profiles.test.factories import ProfileFactory
from profiles.serializers import ProfileSerializer
from patients.test.factories import PatientFactory


# class TestArticleSerializer(TestCase):

    # def setUp(self):
        # tag1 = Tag.objects.create(tag='surgery')
        # tag2 = Tag.objects.create(tag='os')
        # profile = ProfileFactory.create()
        # patient = PatientFactory.create()

        # self._article = ArticleFactory.create(
                # tags=(tag1, tag2), author=profile, patient=patient
            # )

        # self._article_data = model_to_dict(
            # ArticleFactory.create(
                # tags=(tag1, tag2), author=profile, patient=patient
            # )
        # )
        # self._article_data['created'] = self._article.created
        # self._article_data['modified'] = self._article.modified

    # def test_serializer_with_empty_data(self):
        # serializer = ArticleSerializer(data={})
        # eq_(serializer.is_valid(), False)

    # def test_serializer_with_valid_data(self):
        # serializer = ArticleSerializer(data=self._article_data)
        # ok_(serializer.is_valid())


# class TestCommentSerializer(TestCase):

    # def setUp(self):
        # self._comment_data = to_dict(
            # CommentFactory.build()
        # )

    # def test_serializer_with_empty_data(self):
        # serializer = CommentSerializer(data={})
        # eq_(serializer.is_valid(), False)

    # def test_serializer_with_valid_data(self):
        # author = ProfileFactory.create()
        # self._comment_data['author'] = ProfileSerializer(author).data
        # serializer = CommentSerializer(data=self._comment_data)
        # ok_(serializer.is_valid())


class TestTagSerializer(TestCase):

    def setUp(self):
        self._tag_data = to_dict(
            TagFactory.build()
        )

    def test_serializer_with_empty_data(self):
        serializer = TagSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = TagSerializer(data=self._tag_data)
        ok_(serializer.is_valid())

