import pytz

import factory

from django.utils.text import slugify

from ..models import Article, Comment, Tag
from profiles.test.factories import ProfileFactory
from patients.test.factories import PatientFactory


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article

    id = factory.Faker('uuid4')
    title = factory.Faker('sentence')
    description = factory.Faker('text')
    body = factory.Faker('text')
    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)

    author = factory.SubFactory(ProfileFactory)
    patient = factory.SubFactory(PatientFactory)

    @factory.post_generation
    def tags(self, created, extracted, **kwargs):
        if not created:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    id = factory.Faker('uuid4')
    article = factory.SubFactory(ArticleFactory)
    author = factory.SubFactory(ProfileFactory)
    body = factory.Faker('text')

    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Tag

    id = factory.Faker('uuid4')
    tag = factory.Faker('word')

    created = factory.Faker('date_time', tzinfo=pytz.utc)
    modified = factory.Faker('date_time', tzinfo=pytz.utc)
