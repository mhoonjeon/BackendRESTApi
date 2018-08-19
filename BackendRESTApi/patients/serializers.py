from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Patient
        fields = ('id', 'name', 'gender', 'age',)
        read_only_fields = ('gender', )


class CreatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'gender', 'age',)
