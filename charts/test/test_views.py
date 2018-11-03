from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import AdmissionChart, ProgressChart
from .factories import AdmissionChartFactory, ProgressChartFactory
from users.test.factories import UserFactory
from patients.test.factories import PatientFactory
from datetime import datetime, timezone

fake = Faker()


class TestChartViewSetTestCase(APITestCase):
    """
    Tests /charts list operations: basic AND filtering
    Tests /charts post operations.
    """

    def setUp(self):
        self.url = reverse('admissionchart-list')
        self.client.force_authenticate(user=UserFactory.build())

    def test_get_list_request_filtered_with_patient_id_succeeds(self):
        patient = PatientFactory.create()
        AdmissionChartFactory.create_batch(size=3)
        AdmissionChartFactory.create_batch(size=3, patient=patient)
        response = self.client.get(self.url, {'patient': patient.id})
        eq_(len(response.json()['results']), 3)

    def test_get_list_request_filtered_with_created_today_succeeds(self):
        PatientFactory.create()
        AdmissionChartFactory.create_batch(size=3)
        AdmissionChartFactory.create_batch(
            size=3, created=datetime.now(timezone.utc)
        )
        response = self.client.get(self.url, {'created_today': 'true'})
        eq_(len(response.json()['results']), 3)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        patient = PatientFactory.create()
        chart_data = model_to_dict(
            AdmissionChartFactory.build(patient=patient)
        )
        response = self.client.post(self.url, chart_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        chart = AdmissionChart.objects.get(pk=response.data.get('id'))
        eq_(str(chart.patient.id), chart_data.get('patient'))


class TestProgressChartViewSetTestCase(APITestCase):
    """
    Tests /progress_charts list operations: basic AND filtering
    Tests /progress_charts post operations.
    """

    def setUp(self):
        self.url = reverse('progresschart-list')
        self.client.force_authenticate(user=UserFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        admission_chart = AdmissionChartFactory.create()
        chart_data = model_to_dict(ProgressChartFactory.build(
            admission_chart=admission_chart)
        )
        response = self.client.post(self.url, chart_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        chart = ProgressChart.objects.get(pk=response.data.get('id'))
        eq_(chart.id, admission_chart.progress_charts.first().id)
