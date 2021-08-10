from django.shortcuts import render
from django.template import Template , Context
from .models import Slider
from product.models import Category

# Create your views here.
def home(request):
    slider=Slider.objects.filter(active=True)
    categories=Category.objects.filter(product__isnull=False).distinct()
    return render (request, 'home/home.html',{"slider":slider,"categories":categories})
