from company.models import Company
from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from files.models import Image
from django.urls import reverse
from django.utils.safestring import mark_safe

User = get_user_model()

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField()
    parent=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True, blank=True)
    images = GenericRelation(Image)
    def image_tag(self):
        if self.images:
            return mark_safe('<a href="{0}" target="_blank">'
                            '<img src="{1}" width="150" height="150" />'
                            '</a>'.format(self.images.url, self.images['admin_preview'].url)
                            )
        return "-"
    def image_icon(self):
        if self.images:
            return mark_safe('<a href="{0}" target="_blank">'
                            '<img src="{1}" width="100" height="100" />'
                            '</a>'.format(self.images.url, self.images['admin_preview_icon'].url)
                            )
        return "-"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list') + "?category="+str(self.id)


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
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    shipping=models.CharField(max_length=10,choices=PRODUCT_SHIPPING)
    created_At=models.DateTimeField(auto_now_add=True )
    updated_At=models.DateTimeField(auto_now=True )
    images = GenericRelation(Image)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'id':self.id})

    # def get_absolute_url(self):
    #     return "/product/"+str(self.id)

    def __str__ (self):
        return self.name

    
class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='variations')
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=11, decimal_places=2)
    sale_price=models.DecimalField(max_digits=11, decimal_places=2)
    description=models.TextField()
    created_At=models.DateTimeField(auto_now_add=True )
    updated_At=models.DateTimeField(auto_now_add=True )
    images = GenericRelation(Image)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'id':self.product.id})+"? variation=self.id"


    def __str__ (self):
        return self.name

    # def __str__(self):
    #      return "{} {} - {}".format(self.name,self.description,self.price)
