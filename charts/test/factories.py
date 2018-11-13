import pytz

import factory

from ..models import AdmissionChart, ProgressChart
from patients.test.factories import PatientFactory


class ProgressChartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProgressChart

    id = factory.Faker('uuid4')
    # subjective = factory.Faker('text')
    # objective = factory.Faker('text')
    # assessment = factory.Faker('text')
    # plan = factory.Faker('text')
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)


class AdmissionChartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AdmissionChart

    id = factory.Faker('uuid4')
    patient = factory.SubFactory(PatientFactory)
    # cc = factory.Faker('text')
    # pi = factory.Faker('text')
    # pmhx = factory.Faker('text')
    # psxhx = factory.Faker('text')
    # fhx = factory.Faker('text')
    # shx = factory.Faker('text')
    # medications = factory.Faker('text')
    # ros = factory.Faker('text')
    # pe = factory.Faker('text')
    # labs = factory.Faker('text')
    # dx = factory.Faker('text')
    # plan = factory.Faker('text')
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
