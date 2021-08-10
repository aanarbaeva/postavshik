from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    phone= models.CharField("phone number",max_length=40)
    email=models.EmailField('email')
    avatar = ThumbnailerImageField("Фото",upload_to="user/",null=True)
    created_At=models.DateTimeField(auto_now_add=True )
    updated_At=models.DateTimeField(auto_now=True )
    
   
    instagram=models.URLField(("instagram"), max_length=200)
    facebook=models.URLField(("facebook"), max_length=200)
    whatsapp=models.URLField(("whatsapp"), max_length=200)
  

