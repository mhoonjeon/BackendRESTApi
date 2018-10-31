import pytz

import factory

from BackendRESTApi.patients.test.factories import PatientFactory


class AdmissionChartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'charts.AdmissionChart'

    id = factory.Faker('uuid4')
    patient = factory.SubFactory(PatientFactory)
    cc = factory.Faker('lorem')
    pi = factory.Faker('lorem')
    pmhx = factory.Faker('lorem')
    psxhx = factory.Faker('lorem')
    fhx = factory.Faker('lorem')
    shx = factory.Faker('lorem')
    medications = factory.Faker('lorem')
    ros = factory.Faker('lorem')
    pe = factory.Faker('lorem')
    labs = factory.Faker('lorem')
    dx = factory.Faker('lorem')
    plan = factory.Faker('lorem')
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
