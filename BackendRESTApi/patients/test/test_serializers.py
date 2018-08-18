from django.test import TestCase
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import eq_, ok_
from .factories import PatientFactory
from ..serializers import PatientSerializer

class TestCreatePatientSerializer(TestCase):

    def setUp(self):
        self.patient_data = model_to_dict(PatientFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = PatientSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = PatientSerializer(data=self.patient_data)
        ok_(serializer.is_valid())
