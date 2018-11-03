import pytz

import factory

from ..models import Profile
from users.test.factories import UserFactory


class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    id = factory.Faker('uuid4')
    user = factory.SubFactory(UserFactory)

    bio = factory.Faker('text')
    image = factory.Faker('url')

    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
