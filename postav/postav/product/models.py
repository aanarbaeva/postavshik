from company.models import Company
from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField()
    parent=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)


PRODUCT_SHIPPING = [
    ("paid","Paid"),
    ("free","Free"),
    ('self',"Self")
]

PRODUCT_STATUS = [
    ("active","Active"),
    ("inactive","Inactive"),
    ("empty","Empty")
]



class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price=models.DecimalField(max_digits=11, decimal_places=2)
    sale_price=models.DecimalField(max_digits=11, decimal_places=2)
    count= models.IntegerField()
    unit= models.CharField(max_length=120)
    index=models.DecimalField(max_digits=11, decimal_places=2)
    status=models.CharField(max_length=10,choices=PRODUCT_STATUS)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    shipping=models.CharField(max_length=10,choices=PRODUCT_SHIPPING)
    created_At=models.DateTimeField(auto_now_add=True )
    updated_At=models.DateTimeField(auto_now=True )

    


    def __str__(self):
         return "{} {} - {}".format(self.name,self.description,self)