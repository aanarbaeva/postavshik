from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    phone= models.CharField("phone number",max_length=40)
    
    avatar = ThumbnailerImageField("Фото",upload_to="user/",null=True)
    created_At=models.DateTimeField(auto_now_add=True )
    updated_At=models.DateTimeField(auto_now=True )
    
   
    instagram=models.URLField(("instagram"), max_length=200)
    facebook=models.URLField(("facebook"), max_length=200)
    whatsapp=models.URLField(("whatsapp"), max_length=200)
  

class District(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    district=models.ForeignKey(District,on_delete=models.SET_NULL, null=True)
    region=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    street=models.CharField(max_length=120)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{},{},{},{}".format(self.district,self.region,self.city,self.street)

