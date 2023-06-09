from django.contrib import admin
from .models import *

# Register your models here.
class AnswerInline(admin.StackedInline):
    model = Answer

class AnswerAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Category)
admin.site.register(Location)
# admin.site.register(Answer)
admin.site.register(Questions,AnswerAdmin)
admin.site.register(Post)
admin.site.register(PostList)
admin.site.register(RecieverEmailTemplate)
admin.site.register(WishlistProfileService)
admin.site.register(WishlistFeatureService)
admin.site.register(MyResponse)
admin.site.register(PostRequestList)
admin.site.register(RealTimeBookNowService)
admin.site.register(RealTimeBookNow)
admin.site.register(CreditReduceTransaction)