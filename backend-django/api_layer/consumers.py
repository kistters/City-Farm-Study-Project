import random
from urllib.parse import parse_qs

from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.db.models import Count


def update_websocket_dashboard(text):

    message = {
        'type': 'echo',
        'message': f"{text}"
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('broadcast', message)


class StatusConsumer(JsonWebsocketConsumer):
    groups = ['broadcast']
    token = None

    def websocket_connect(self, message):
        # ws://api.cityfarm.com/ws/status/?connect_to=chicken,corn #multiple
        # ws://api.cityfarm.com/ws/status/chicken/ #uniq
        # ws://api.cityfarm.com/ws/status/ listen all
        try:
            query_string = self.scope['query_string'].decode()
            if query_string:
                parameters = parse_qs(query_string)
                self.token = parameters.get('token', [None])[0]

            self.groups = [self.scope['url_route']['kwargs']['name']]
        except KeyError as e:
            pass
        # self.channel_name = self.token
        super().websocket_connect(message)

    def connect(self):
        self.accept()
        content = {
            "type": "echo.message",
            'by': self.token,
            "message": f"{self.token} is connected!"
        }
        async_to_sync(self.channel_layer.group_send)('broadcast', content)
        # self.send_json({
        #     "groups": self.groups,
        #     'token': self.token,
        #     'private': self.channel_name}
        # )

    def disconnect(self, code):
        content = {
            "type": "echo.message",
            'by': self.token,
            "message": f"{self.token}is disconnected! [{code}]"
        }
        async_to_sync(self.channel_layer.group_send)('broadcast', content)

    def receive_json(self, content, **kwargs):
        """ websocket payload with extra groups to broadcast
        {"type": "echo", "groups": ["chicken"], "message":"Hello There!"}
        """
        groups = [group for group in set(self.groups + content.get('groups', [])) if group]
        content.update({'by': self.token})
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
        if content.get('by') == self.token:
            return

        self.send_json(content=f"{content.get('by')}: {content.get('message')}")
