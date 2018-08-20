from django.test import TestCase
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import eq_, ok_
from .factories import SentenceFactory
from ..serializers import SentenceSerializer
from BackendRESTApi.charts.test.factories import ChartFactory

class TestCreateSentenceSerializer(TestCase):

    def setUp(self):
        self.sentence_data = model_to_dict(SentenceFactory.create())

    def test_serializer_with_empty_data(self):
        serializer = SentenceSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = SentenceSerializer(data=self.sentence_data)
        ok_(serializer.is_valid())
