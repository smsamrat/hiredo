from .serializers import MessageSerializer,InboxSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth import get_user_model


class MessageView(APIView):
    def get(self, request, id, format=None):
        user = request.user
        other_user = get_user_model().objects.get(id=id)
        obj = Thread.objects.get_or_create_personal_thread(self.request.user.id, other_user)
        messages = obj.message_set.filter(user=self.request.user,recipient=other_user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ThreadSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse
import json
class InboxView(APIView):
    def get(self, request, format=None):
        messages = Message.get_messages(user=request.user)
        # unread = []
        # time = []
        # for i in messages:
        #     unread.append(i['unread'])
        #     time.append(i['last'])
        
        # 'unread':unread,'time':time
            

        
        serializer = InboxSerializer(messages,many=True)
        return Response({'messages':serializer.data,}, status=status.HTTP_200_OK)
    


   

# def msg_inbox(request):
#     messages = Message.get_messages(user=request.user)
#     active_direct = None
#     directs = None

#     if messages:
#         message = messages[0]
#         active_direct = message['user'].username
#         directs = Message.objects.filter(user=request.user, recipient=message['user'])
#         directs.update(is_read=True)
#         for message in messages:
#             if message['user'].username == active_direct:
#                 message['unread'] = 0

#     context = {
#     'directs': directs,
#     'messages': messages,
#     'active_direct': active_direct,
#     }
    
    
#     return render(request, 'chat/inbox.html',context)