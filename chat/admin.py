from django.contrib import admin
from chat.models import Message, Thread


class MessageInline(admin.StackedInline):
    model = Message
    fields = ('sender', 'text')
    readonly_fields = ('sender', 'text')

# fields = ('user', 'recipient','body','is_read',)
#     readonly_fields = ('user', 'recipient','body','is_read',)

class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = (MessageInline,)

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message)
# admin.site.register(Messages)