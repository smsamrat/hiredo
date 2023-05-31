from channels.consumer import SyncConsumer,AsyncConsumer
from asgiref.sync import async_to_sync,sync_to_async
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import *
import json

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        me = self.scope['user']
        print(me)
        other_user_id = self.scope['url_route']['kwargs']['id']
        self.other_user = await sync_to_async(get_user_model().objects.get)(id=other_user_id)
        print(self.other_user.id)
        self.thread_obj = await sync_to_async(Thread.objects.get_or_create_personal_thread)(me,self.other_user.id)

        self.room_name = f'thread_name_{self.thread_obj.id}'

        await self.channel_layer.group_add(self.room_name,self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
        print(f'[{self.channel_name}] - you are connected' )

    async def websocket_receive(self,event):
        print(f'[{self.channel_name}] - you are Received message - {event.get("text")}')

        msg = json.dumps({
            'text':event.get('text'),
            'username': self.scope['user'].id
        })

        await self.store_message(event.get("text"))

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type':'websocket.message',
                'text':msg
            }
                                                    
        )

    async def websocket_message(self,event):
        print(f'[{self.channel_name}] - send message ' )
        await self.send(
            {
                'type':'websocket.send',
                'text':event.get('text'),
            }
        )


    async def websocket_disconnect(self,event):
        print(f'[{self.channel_name}] - Disconnected' )
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    @database_sync_to_async
    def store_message(self, text):
        Message.send_message(self.thread_obj,self.scope['user'],self.other_user,text)
        # Message.send_message(thread,from_user, to_user, body)
        

