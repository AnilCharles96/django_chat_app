from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json
from newapp.views import current_user
from django.contrib.auth import get_user_model
from .models import Message, Chat

User = get_user_model()
class ChatConsumer(AsyncWebsocketConsumer):
     async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

     async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
     async def receive(self, text_data):
        message_str = ''
        check = []
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room = text_data_json['room_name']
        user = self.scope['user']  

        chat_obj = Chat.objects.get(name=room)
        if message:
            Message.objects.create(chat_room=chat_obj,author=user,content=message)

            # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                    'type': 'chat_message',
                    'message': message
            }
        )

    # Receive message from room group
     async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

       