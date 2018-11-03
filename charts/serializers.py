from rest_framework import serializers
from .models import AdmissionChart, ProgressChart
from patients.serializers import PatientSerializer


class CreateAdmissionChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdmissionChart
        fields = '__all__'


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
