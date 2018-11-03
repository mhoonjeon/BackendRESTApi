import random
import string

from django.db.models.fields.related import ManyToManyField

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits


def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
    return ''.join(random.choice(chars) for _ in range(size))


def to_dict(instance):
    """
    https://stackoverflow.com/questions/21925671/\
    convert-django-model-object-to-dict-with-all-of-the-fields-intact
    """
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(
                    f.value_from_object(instance).values_list('pk', flat=True)
                )
        else:
            data[f.name] = f.value_from_object(instance)
    return data
