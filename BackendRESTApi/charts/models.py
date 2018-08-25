from model_utils.models import TimeStampedModel
import uuid

from django.db import models


class Chart(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name="charts")

    class Meta:
        ordering = ['-id']
