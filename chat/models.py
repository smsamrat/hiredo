from chat.managers import ThreadManager
from django.db import models
from django.db.models import Q, Max
from django.contrib.auth import get_user_model

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Thread(TrackingModel):
    THREAD_TYPE = (
        ('personal', 'Personal'),
        ('group', 'Group')
    )

    name = models.CharField(max_length=50, null=True, blank=True)
    thread_type = models.CharField(max_length=15, choices=THREAD_TYPE, default='group')
    users = models.ManyToManyField('account.User')

    objects = ThreadManager()

    # def __str__(self) -> str:
    #     if self.thread_type == 'personal' and self.users.count() == 2:
    #         return f'{self.users.first()}_and_{self.users.last()}'
    #     return f'{self.name}'
    

class Message(TrackingModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='userss',blank=True, null=True,)
    sender = models.ForeignKey('account.User', on_delete=models.CASCADE)
    recipient = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='recipient_user',blank=True, null=True) 
    text = models.TextField(blank=False, null=False)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True,null=True)
    
    def send_message(thread,from_user, to_user, text):
        sender_message = Message(
            thread = thread,
            user=from_user,
            sender=from_user,
            recipient=to_user,
            text=text,
            is_read=True)
        sender_message.save()

        recipient_message = Message(
            thread = thread,
            user=to_user,
            sender=from_user,
            text=text,
            recipient=from_user)
        recipient_message.save()
        return sender_message
    
    def get_messages(user):
        messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
        users = []
        for message in messages:
            users.append({
                'user': get_user_model().objects.get(pk=message['recipient']),
                # 'last': message['last'],
                # 'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
                })
        return users
    
    
    
    def __str__(self) -> str:
        return f'From <Thread - {self.thread}>'
    
