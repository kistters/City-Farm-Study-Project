from django.urls import path

from api_layer.consumers import StatusConsumer

websocket_urlpatterns = [
    path('ws/status/', StatusConsumer.as_asgi(), name='status'),
]
