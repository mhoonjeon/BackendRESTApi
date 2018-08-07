from model_utils import Choices
from model_utils.models import TimeStampedModel
import uuid

from django.db import models


class Patient(TimeStampedModel):
    MALE = 0
    FEMALE = 1
    GENDER = Choices((MALE, '남성'), (FEMALE, '여성'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    gender = models.BooleanField(choices=GENDER, default=MALE)
    age = models.PositiveSmallIntegerField()
