from pyexpat import model
from attr import field
from django.contrib import admin
from .models import Images

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','images','date']
    
