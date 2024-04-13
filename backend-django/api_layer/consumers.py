import random

from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.db.models import Count


def update_websocket_dashboard():

    message = {
        'type': 'broadcast_message',
        'message': {
            'random': random.randint(1, 1000),
        }
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('broadcast', message)


class StatusConsumer(JsonWebsocketConsumer):
    groups = ['broadcast']

    def websocket_connect(self, message):
        # ws://api.cityfarm.com/ws/status/?connect_to=chicken,corn #multiple
        # ws://api.cityfarm.com/ws/status/chicken/ #uniq
        # ws://api.cityfarm.com/ws/status/ listen all
        try:
            self.groups = [self.scope['url_route']['kwargs']['name']]
        except KeyError as e:
            pass
        super().websocket_connect(message)

    def connect(self):
        self.accept()
        self.send_json({"message": "Accept", "groups": self.groups})

    def receive_json(self, content, **kwargs):
        """ websocket payload with extra groups to broadcast
        {"type": "echo", "groups": ["chicken"], "message":"Hello There!"}
        """
        groups = [group for group in set(self.groups + content.get('groups', [])) if group]

        for group in groups:
            async_to_sync(self.channel_layer.group_send)(group, content)

    def echo(self, content):
        """ websocket payload example
        {"type": "echo", "message":"Hello There!"}
        """
        self.send_json(content=content)

    def echo_message(self, content):
        """ websocket payload example
        {"type": "echo.message", "message":"Hello There!"}
        """
        self.send_json(content=content.get('message'))
