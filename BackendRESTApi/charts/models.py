from model_utils.models import TimeStampedModel
import uuid

from django.db import models


class AbstractChart(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created']


class AdmissionChart(AbstractChart):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE,
                                related_name="admission_charts")
    cc = models.TextField(null=True, blank=True)
    pi = models.TextField(null=True, blank=True)
    pmhx = models.TextField(null=True, blank=True)
    psxhx = models.TextField(null=True, blank=True)
    fhx = models.TextField(null=True, blank=True)
    shx = models.TextField(null=True, blank=True)
    medications = models.TextField(null=True, blank=True)
    ros = models.TextField(null=True, blank=True)
    pe = models.TextField(null=True, blank=True)
    labs = models.TextField(null=True, blank=True)
    dx = models.TextField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)


class ProgressChart(AbstractChart):
    admission_chart = models.ForeignKey(AdmissionChart, on_delete=models.CASCADE,
                                related_name="progress_charts")
    subjective = models.TextField(null=True, blank=True)
    objective = models.TextField(null=True, blank=True)
    assessment = models.TextField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)
