import uuid

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.db import models

CATEGORIES = Choices(
    ('CC', 'Chief Complaint'),
    ('PI', 'Present Illness'),
    ('PMH', 'Past Medical History'),
    ('FH', 'Family History'),
    ('SH', 'Social History'),
    ('ROS', 'Review of System')
)


class Sentence(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chart = models.ForeignKey('charts.Chart', on_delete=models.CASCADE, related_name="sentences")
    raw = models.CharField(max_length=1024)
    category = models.CharField(max_length=5, choices=CATEGORIES, null=True)

    class Meta:
        ordering = ['-id']
