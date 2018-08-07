from model_utils.models import TimeStampedModel
import uuid

from django.db import models


class Chart(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name="charts")
    # cc = models.CharField(max_length=255)
    # pi = models.TextField()


# class PastMedicalHistory(TimeStampedModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # chart = models.ForeignKey("Chart", on_delete=models.CASCADE, related_name="past_medical_histories")


# class PersonalHistory(TimeStampedModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # chart = models.ForeignKey("Chart", on_delete=models.CASCADE, related_name="personal_histories")


# class ReviewOfSystem(TimeStampedModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # chart = models.ForeignKey("Chart", on_delete=models.CASCADE, related_name="ROS")


# class PhysicalFinding(TimeStampedModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # chart = models.ForeignKey("Chart", on_delete=models.CASCADE, related_name="PE")
