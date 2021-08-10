from django.contrib import admin
from .models import Image
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # list_display=["id",image_icon","file","alt"]
    # fields=["file","alt","variation"]
    # readonly_fields=["image_icon"]
    pass
class ImageInline(GenericTabularInline):
    model = Image
   
    min_num=1
    extra=0
  
    
