import uuid

from model_utils import Choices
from model_utils.models import TimeStampedModel
# from simple_history.models import HistoricalRecords

from django.db import models

CATEGORIES = Choices(
    (0, 'CC', _('Chief Complaint')),
    (1, 'PI', _('Present Illness')),
    (2, 'PMH', _('Past Medical History')),
    (3, 'FH', _('Family History')),
    (4, 'SH', _('Social History')),
    (5, 'ROS', _('Review of System'))
)


class Sentence(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chart = models.ForeignKey('charts.Chart', on_delete=models.CASCADE, related_name="sentences")
    category = models.CharField(max_length=5, choices=CATEGORIES, null=True)
    raw_sentence = models.CharField(max_length=1024)
    deep_output = models.CharField(max_length=1024)
    final_sentence = models.CharField(max_length=1024)
    # history = HistoricalRecords()
