from django.urls import path

from .consumers import ClientConsumer

websocket_urlpatterns = [
    path('ws/v1/transcriptions/client/<str:patient_id>/', ClientConsumer),
]
