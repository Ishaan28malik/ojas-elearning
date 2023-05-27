from django.contrib import admin
from . models import Tutorial, Member
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]
    formfield_overrides = { 
        models.TextField: {'widget': TinyMCE()},
        }
       
class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ("name/origin", {'fields': ["member_name", "member_origin"]}),
        ("Content", {"fields": ["member_details"]})
    ]
    formfield_overrides = { 
        models.TextField: {'widget': TinyMCE()},
        }
       


admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Member,MemberAdmin)

