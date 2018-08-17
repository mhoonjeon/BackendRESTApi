import factory

from ..models import Patient


class PatientFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'patients.Patient'
        django_get_or_create = ('name',)

    id = factory.Faker('uuid4')
    name = factory.Sequence(lambda n: f'testpatient{n}')
    gender = factory.Iterator([Patient.MALE, Patient.FEMALE])
    age = factory.fuzzy.FuzzyInteger(0,150)
    created = factory.Faker('date_time')
    modified = factory.Faker('date_time')
