import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):
    """ handle async websocket"""
    room_name = None
    room_group_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # joining the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # accept the connection
        await self.accept()

    async def disconnect(self):
        # leave the group
        if self.room_group_name and self.channel_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    # recieve the message
    async def recieve(self, text_data=None, bytes_data=None):
        event = json.loads(text_data)
        message = event['message']

        # send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.scope['user'].username.title(),
                'message': message
            }
        )
    # broadcast the message
    async def  chat_message(self, event):
        message = event['message']
        username = event['username']

        # send back the message
        await self.send(text_data = json.dumps({
            'message': message,
            'username': username
        }))


