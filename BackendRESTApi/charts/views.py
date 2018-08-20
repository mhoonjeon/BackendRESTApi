from datetime import date
from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Chart
from .serializers import GetChartSerializer


def created_today( queryset, name, value):
    if value == True:
        return queryset.filter(created__date=date.today())


class ChartFilter(filters.FilterSet):
    created_today = filters.BooleanFilter(field_name='created__date',
                                           method=created_today)

    class Meta:
        model = Chart
        fields = ['patient', 'created_today']


class ChartViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    queryset = Chart.objects.all()
    serializer_class = GetChartSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ChartFilter
