from model_utils.models import TimeStampedModel
import uuid

from django.db import models


class Sentence(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    charts = models.ForeignKey("charts.Chart", on_delete=models.CASCADE,
                               related_name="sentences")
    content = models.CharField(max_length=256)
