from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import ChartFactory
from ..serializers import ChartSerializer
from BackendRESTApi.charts.test.factories import ChartFactory

class TestCreateChartSerializer(TestCase):

    def setUp(self):
        self.chart_data = model_to_dict(ChartFactory.create())

    def test_serializer_with_empty_data(self):
        serializer = ChartSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ChartSerializer(data=self.chart_data)
        ok_(serializer.is_valid())
