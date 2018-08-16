from django.urls import path

from .consumers import ClientConsumer, DeepConsumer

websocket_urlpatterns = [
    path('ws/v1/transcriptions/client/<str:patient_id>/', ClientConsumer),
    path('ws/v1/transcriptions/deep/<str:patient_id>/', DeepConsumer)
]
