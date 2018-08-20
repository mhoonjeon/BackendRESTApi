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
        ChartFactory.create_batch(size=3, created=datetime.now())
        response = self.client.get(self.url, {'created_today': 'true'} )
        eq_(len(response.json()['results']), 3)