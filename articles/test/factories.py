import pytz

import factory

from ..models import Article, Comment, Tag
from patients.test.factories import PatientFactory


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article

    id = factory.Faker('uuid4')
    slug = factory.Faker('slug')
    title = factory.Faker('title')
    description = factory.Faker('text')
    body = factory.Faker('text')
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)

    author = factory

class AdmissionChartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AdmissionChart

    id = factory.Faker('uuid4')
    patient = factory.SubFactory(PatientFactory)
    cc = factory.Faker('text')
    pi = factory.Faker('text')
    pmhx = factory.Faker('text')
    psxhx = factory.Faker('text')
    fhx = factory.Faker('text')
    shx = factory.Faker('text')
    medications = factory.Faker('text')
    ros = factory.Faker('text')
    pe = factory.Faker('text')
    labs = factory.Faker('text')
    dx = factory.Faker('text')
    plan = factory.Faker('text')
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
