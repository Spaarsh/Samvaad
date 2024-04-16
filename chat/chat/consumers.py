from channels.generic.websocket import AsyncWebsocketConsumer
from users.models import Message, User
from rooms.models import Room
import json
from django.utils import timezone
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(f"Connecting to room: {self.room_name}")
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        print(f"Joining group: {self.room_group_name}")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print("Connection accepted")
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        print(f"Leaving group: {self.room_group_name}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(f"Received message: {text_data_json}")
        message = text_data_json['message']
        user_id = text_data_json['user_id']
        print(f"User id: {user_id}")

        room = await self.get_room()
        user = await self.get_user(user_id)
        await self.create_message(room, user, message)

        print(f"this is the user: {user}")
        

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    @database_sync_to_async
    def get_room(self):
        return Room.objects.get(name=self.room_name)

    @database_sync_to_async
    def get_user(self, user_id):
        print(f"Getting user with id: {user_id}")
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    @database_sync_to_async
    def create_message(self, room, user, message):
        print(user, room, message)
        return Message.objects.create(
            room_id=room.id,
            user_id=user.id,
            timestamp=timezone.now(),
            content=message,
        )
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))