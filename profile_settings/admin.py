from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from lead.models import Post


# Register your models here.
class HelpAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

class HelpAdmin(admin.ModelAdmin):
    form = HelpAdminForm


admin.site.register(Badge)
# admin.site.register(About)
# admin.site.register(Photo)
# admin.site.register(Social_Media_Link)
admin.site.register(Elit_Pro)
admin.site.register(Account_Details )
admin.site.register(ReviewRating)
admin.site.register(Profile)
admin.site.register(HelpTopic)
admin.site.register(Help, HelpAdmin)
admin.site.register(StillNeedHelp)
