from rest_framework import serializers
from .models import AdmissionChart, ProgressChart
from patients.models import Patient
from patients.serializers import PatientSerializer


class CreateAdmissionChartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = AdmissionChart
        fields = '__all__'

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        patient = Patient.objects.get_or_create(**patient_data)

        admission_chart = AdmissionChart.objects.create(patient=patient, **validated_data)

        return admission_chart

    def update(self, instance, validated_data):
        patient_data = validated_data.pop('patient')
        patient = instance.patient

        instance.note = validated_data.get('note', instance.note)
        instance.save()

        patient = Patient.objects.get_or_create(**patient_data)

        if not patient:
            patient.name = patient_data.get('name', patient.name)
            patient.gender = patient_data.get('gender', patient.gender)
            patient.age = patient_data.get('age', patient.age)

            patient.save()

        return instance

class CreateProgressChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgressChart
        fields = '__all__'


class GetProgressChartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    created = serializers.DateTimeField(format="%Y년 %m월 %d일")
    modified = serializers.DateTimeField(format="%Y년 %m월 %d일")

    class Meta:
        model = ProgressChart
        fields = '__all__'


class GetAdmissionChartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    progress_charts = GetProgressChartSerializer(many=True)
    created = serializers.DateTimeField(format="%Y년 %m월 %d일")
    modified = serializers.DateTimeField(format="%Y년 %m월 %d일")
    progress_charts = GetProgressChartSerializer(required=False, many=True)

    class Meta:
        model = AdmissionChart
        fields = '__all__'
