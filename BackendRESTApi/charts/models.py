import uuid

from django.db import models


class Chart(models):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('patients.Patient', related_name="charts")
    cc = models.CharField(max_length=255)
    pi = models.TextField()


class PastMedicalHistory(models):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey("Note", related_name="past_medical_histories")


class PersonalHistory(models):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey("Note", related_name="personal_histories")


class ReviewOfSystem(models):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey("Note", related_name="ROS")


class PhysicalFinding(models):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey("Note", related_name="PE")
