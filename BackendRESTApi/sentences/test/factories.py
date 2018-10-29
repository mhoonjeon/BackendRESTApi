import pytz

import random

import factory

from ..models import Sentence, CATEGORIES
from BackendRESTApi.charts.test.factories import ChartFactory


def get_category():
    category_choices = [x[0] for x in CATEGORIES]
    return random.choice(category_choices)


class SentenceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'sentences.Sentence'

    id = factory.Faker('uuid4')
    chart = factory.SubFactory(ChartFactory)
    raw = factory.Faker('sentence')
    category = factory.LazyFunction(get_category)
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
