from django.contrib import admin
from .models import Editor,Pics,tags

# Register your models here.

class PicsAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Pics,PicsAdmin)
admin.site.register(tags)
