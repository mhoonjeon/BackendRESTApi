from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_

from core.utils import to_dict
from .factories import ProfileFactory
from ..serializers import ProfileSerializer
from users.models import User
from users.test.factories import UserFactory


class TestProfileChartSerializer(TestCase):

    def setUp(self):
        user = UserFactory.create()
        self.profile_data = model_to_dict(ProfileFactory.build(user=user))

    def test_serializer_with_empty_data(self):
        serializer = ProfileSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        self.profile_data['username'] = User.objects.get(
            id=self.profile_data['user']
        ).username
        serializer = ProfileSerializer(data=self.profile_data)
        ok_(serializer.is_valid())
