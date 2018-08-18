from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import Patient
from .factories import PatientFactory

fake = Faker()


class TestPatientPostTestCase(APITestCase):
    """
    Tests /patients/ post operations.
    """

    def setUp(self):
        self.url = reverse('patient-post')
        self.patient_data = model_to_dict(PatientFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.patient_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        patient = Patient.objects.get(pk=response.data.get('id'))
        eq_(patient.name, self.patient_data.get('name'))
