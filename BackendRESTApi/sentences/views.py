from django_filters import rest_framework as filters

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Sentence
from .serializers import SentenceSerializer


class SentenceViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):

    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('chart', )

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
