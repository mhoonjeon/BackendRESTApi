from model_utils.models import TimeStampedModel
from uuid

from django.db import models


class Sentence(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    charts = models.ForeignKey("charts.Chart", related_name="sentences")
    content = models.CharField(max_length=256)
