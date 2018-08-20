import pytz
import random

import factory

from ..models import Chart
from BackendRESTApi.patients.test.factories import PatientFactory

class ChartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'charts.Chart'

    id = factory.Faker('uuid4')
    patient = factory.SubFactory(PatientFactory)
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
