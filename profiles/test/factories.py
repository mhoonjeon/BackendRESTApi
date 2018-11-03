import pytz
import factory

from django.db.models.signals import post_save

from ..models import Profile


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    id = factory.Faker('uuid4')
    user = factory.SubFactory('users.test.factories.UserFactory', profile=None)

    bio = factory.Faker('text')
    image = factory.Faker('url')

    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)


class ProfileFactoryForAuth(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    id = factory.Faker('uuid4')
    user = factory.SubFactory('users.test.factories.UserFactory')

    bio = factory.Faker('text')
    image = factory.Faker('url')

    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
