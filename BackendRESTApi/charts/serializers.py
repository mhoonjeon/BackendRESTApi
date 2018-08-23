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
    patient_name = serializers.CharField(source='patient.name')
    patient_id = serializers.CharField(source='patient.id')
    patient_cc = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")
    modified = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Chart
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = kwargs['context']['request']
        remove_patient_name = request.GET.get('patient', False)
        if remove_patient_name:
            self.fields.pop('patient_name', None)
            self.fields.pop('patient', None)

    def get_patient_cc(self, object):
        try:
            # Two of more sentences are mapped to CC
            patient_cc = object.sentences.filter(category='CC')[:1].get()
            return patient_cc.raw
        except Sentence.DoesNotExist:
            return None
