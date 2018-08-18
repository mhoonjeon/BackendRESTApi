import pytz
import random

import factory

from ..models import Patient


def get_age():
    age_choices = [x[0] for x in Patient.GENDER]
    return random.choice(age_choices)

class PatientFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'patients.Patient'
        django_get_or_create = ('name',)

    id = factory.Faker('uuid4')
    name = factory.Sequence(lambda n: f'testpatient{n}')
    gender = factory.Iterator([Patient.MALE, Patient.FEMALE])
    age = factory.LazyFunction(get_age)
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
