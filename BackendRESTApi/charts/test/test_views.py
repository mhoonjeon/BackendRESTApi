from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import Chart
from .factories import ChartFactory
from BackendRESTApi.users.test.factories import UserFactory
from BackendRESTApi.patients.test.factories import PatientFactory
from BackendRESTApi.sentences.test.factories import SentenceFactory
from datetime import datetime

fake = Faker()


class TestChartListTestCase(APITestCase):
    """
    Tests /charts list operations.
    """

    def setUp(self):
        self.url = reverse('chart-list')
        self.client.force_authenticate(user=UserFactory.build())

    def test_get_list_request_filtered_with_patient_id_succeeds(self):
        patient = PatientFactory.create()
        ChartFactory.create_batch(size=3)
        ChartFactory.create_batch(size=3, patient=patient)
        response = self.client.get(self.url, {'patient': patient.id} )
        eq_(len(response.json()['results']), 3)

    def test_get_list_request_filtered_with_created_succeeds(self):
        patient = PatientFactory.create()
        ChartFactory.create_batch(size=3)
        now = datetime.now()
        ChartFactory.create_batch(size=3, created=now)
        for chart in Chart.objects.filter(created=now):
            SentenceFactory.create(chart=chart, category='CC')
            SentenceFactory.create(chart=chart, category='CC')
        response = self.client.get(self.url, {'created_today': 'true'} )
        self.assertIn('patient_id', response.json()['results'][0])
        self.assertIn('patient_name', response.json()['results'][0])
        self.assertIn('patient_cc', response.json()['results'][0])
        eq_(len(response.json()['results']), 3)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        patient = PatientFactory.create()
        chart_data = model_to_dict(ChartFactory.build(patient=patient))
        response = self.client.post(self.url, chart_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        chart = Chart.objects.get(pk=response.data.get('id'))
        eq_(str(chart.patient.id), chart_data.get('patient'))
