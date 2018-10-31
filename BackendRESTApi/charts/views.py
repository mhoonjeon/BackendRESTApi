from datetime import date
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import AdmissionChart, ProgressChart
from .serializers import (
    GetAdmissionChartSerializer, CreateAdmissionChartSerializer,
    CreateProgressChartSerializer, GetProgressChartSerializer
)

def created_today( queryset, name, value):
    if value == True:
        return queryset.filter(created__date=date.today())


class ChartFilter(filters.FilterSet):
    created_today = filters.BooleanFilter(field_name='created__date',
                                           method=created_today)

    class Meta:
        model = AdmissionChart
        fields = ['patient', 'created_today']


class ChartViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):

    queryset = AdmissionChart.objects.all()
    serializer_class = GetAdmissionChartSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ChartFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAdmissionChartSerializer
        return super().get_serializer_class()


class ProgressChartViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):

    queryset = ProgressChart.objects.all()
    serializer_class = GetProgressChartSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProgressChartSerializer
        return super().get_serializer_class()
