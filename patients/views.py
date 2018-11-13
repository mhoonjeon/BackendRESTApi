from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer, CreatePatientSerializer


class PatientViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePatientSerializer
        return super().get_serializer_class()
