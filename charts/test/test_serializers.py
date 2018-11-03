from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_

from core.utils import to_dict
from .factories import AdmissionChartFactory, ProgressChartFactory
from ..serializers import (
    CreateAdmissionChartSerializer, CreateProgressChartSerializer,
    GetAdmissionChartSerializer, GetProgressChartSerializer
)
from patients.test.factories import PatientFactory


class TestCreateAdmissionChartSerializer(TestCase):

    def setUp(self):
        self.chart_data = model_to_dict(AdmissionChartFactory.create())

    def test_serializer_with_empty_data(self):
        serializer = CreateAdmissionChartSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        patient = PatientFactory.build()
        self.chart_data['patient'] = model_to_dict(patient)
        serializer = CreateAdmissionChartSerializer(data=self.chart_data)
        ok_(serializer.is_valid())


class TestCreateProgressChartSerializer(TestCase):

    def setUp(self):
        admission_chart = AdmissionChartFactory.create()
        self.chart_data = model_to_dict(
            ProgressChartFactory.create(admission_chart=admission_chart)
        )

    def test_serializer_with_empty_data(self):
        serializer = CreateProgressChartSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateProgressChartSerializer(data=self.chart_data)
        ok_(serializer.is_valid())


class TestGetAdmissionChartSerializer(TestCase):

    def setUp(self):
        self.chart_data = model_to_dict(AdmissionChartFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = GetAdmissionChartSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data_without_progress_charts(self):
        admission_chart = to_dict(AdmissionChartFactory.build())
        serializer = GetAdmissionChartSerializer(data=admission_chart)
        ok_(serializer.is_valid())

    def test_serializer_with_valid_data_with_progress_charts(self):
        admission_chart = AdmissionChartFactory.create()
        ProgressChartFactory.create_batch(
            size=3, admission_chart=admission_chart
        )

        admission_chart_data = to_dict(admission_chart)
        admission_chart_data['progress_charts'] = CreateProgressChartSerializer(
            admission_chart.progress_charts.all(),
            many=True
        ).data
        serializer = GetAdmissionChartSerializer(data=admission_chart_data)
        ok_(serializer.is_valid())
        eq_(len(serializer.data['progress_charts']), 3)


class TestGetProgressChartSerializer(TestCase):

    def setUp(self):
        admission_chart = AdmissionChartFactory.create()
        self.chart_data = to_dict(
            ProgressChartFactory.build(admission_chart=admission_chart)
        )

    def test_serializer_with_empty_data(self):
        serializer = GetProgressChartSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = GetProgressChartSerializer(data=self.chart_data)
        ok_(serializer.is_valid())
