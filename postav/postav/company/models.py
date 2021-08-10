from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


TYPE_COMPANY = [
    ("pub","Public"),
    ("pri","Private"),
    ]

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    created_At=models.DateTimeField(auto_now_add=True )
    updated_At=models.DateTimeField(auto_now=True )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=3,choices=TYPE_COMPANY)
    longitude = models.CharField(max_length=40) 
    latitude = models.CharField(max_length=40)

    instagram=models.URLField(("instagram"), max_length=200)
    facebook=models.URLField(("facebook"), max_length=200)
    whatsapp=models.URLField(("whatsapp"), max_length=200)
  


    # def __str__(self):
    #      return "{} {} - {}".format(self.name,self.description)