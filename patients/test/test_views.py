from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import Patient
from .factories import PatientFactory

from users.test.factories import UserFactory

fake = Faker()


class TestPatientPostTestCase(APITestCase):
    """
    Tests /patients list operations.
    """

    def setUp(self):
        self.url = reverse('patient-list')
        self.patient_data = model_to_dict(PatientFactory.build())
        self.client.force_authenticate(user=UserFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.patient_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        patient = Patient.objects.get(pk=response.data.get('id'))
        eq_(patient.name, self.patient_data.get('name'))

    def test_get_list_request_succeeds(self):
        PatientFactory.create_batch(size=3)
        response = self.client.get(self.url)
        eq_(len(response.json()['results']), 3)


class TestUserDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """

    def setUp(self):
        PatientFactory.create_batch(size=4)
        self.patient_id = Patient.objects.first().id
        self.url = reverse('patient-detail', kwargs={'pk': self.patient_id})
        self.client.force_authenticate(user=UserFactory.build())

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)
        eq_(response.json()['id'], str(self.patient_id))
