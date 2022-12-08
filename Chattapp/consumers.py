import json
from django.contrib.auth.mixins import LoginRequiredMixin
from channels.generic.websocket import AsyncWebsocketConsumer
#from asgiref.sync import async_to_sync
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer, LoginRequiredMixin):
    async def connect(self):  # called when a new connection is received.
        self.user = self.scope['user']
        await self.channel_layer.group_add('main_group_chat', self.channel_name)
        await self.accept()

    async def disconnect(self, code):  # called when the socket is closed.
        await self.channel_layer.group_discard('main_group_chat', self.channel_name)

    async def receive(self, text_data):
        """Called whenever data is received"""
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        await self.channel_layer.group_send('main_group_chat', {
            'type': 'chat_message',
            'message': message,
            'user': self.user.username,
            'datetime': now.isoformat(),
        })
        # self.send(text_data=json.dumps({'message': message}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
