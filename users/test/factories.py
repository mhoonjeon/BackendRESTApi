import factory

from django.db.models.signals import post_save

from profiles.test.factories import ProfileFactory


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker(
        'password', length=10, special_chars=True,
        digits=True, upper_case=True, lower_case=True
    )
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False

    profile = factory.RelatedFactory(ProfileFactory, 'user')


class UserFactoryForAuth(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker(
        'password', length=10, special_chars=True,
        digits=True, upper_case=True, lower_case=True
    )
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
