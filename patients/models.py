from model_utils import Choices
from model_utils.models import TimeStampedModel
import uuid

from django.db import models


class Patient(TimeStampedModel):
    MALE = 'male'
    FEMALE = 'female'
    GENDER = Choices((MALE, 'male'), (FEMALE, 'female'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    gender = models.CharField(
        choices=GENDER, max_length=5,
        default=MALE, blank=True, null=True
    )
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-id']
