from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Maqola,Rasm
@admin.register(Maqola)
class MaqolaAdmin(ModelAdmin):
    search_fields = ['id','title','matn','time']
    list_display = ['title','matn','time']
admin.site.register(Rasm)
# Register your models here.
