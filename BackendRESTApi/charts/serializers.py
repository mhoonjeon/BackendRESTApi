from rest_framework import serializers
from .models import Chart
from BackendRESTApi.patients.serializers import PatientSerializer
from BackendRESTApi.sentences.serializers import SentenceSerializer
from BackendRESTApi.sentences.models import Sentence


class CreateChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chart
        fields = '__all__'


class GetChartSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    cc = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")
    modified = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Chart
        fields = '__all__'

    def get_cc(self, object):
        try:
            # Two of more sentences may be mapped to CC
            patient_cc = object.sentences.filter(category='CC')[:1].get()
            return patient_cc.raw
        except Sentence.DoesNotExist:
            return None
