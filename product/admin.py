from django.contrib.admin.options import TabularInline
from files.admin import ImageInline
from django.contrib import admin
from product.models import Product, Variation, Category
from jet.admin import CompactInline


# Register your models here.
class InlineVariation(CompactInline):
    model=Variation
    min_num=1
    extra=0
    show_change_link=True


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=["name","description"]
    inlines=[InlineVariation,ImageInline]



@admin.register(Variation)
class AdminVariation(admin.ModelAdmin):
    list_display=["name","description","price","sale_price","created_At","updated_At"]
    inlines=[ImageInline]
   
class InlineProduct(CompactInline):
    model = Product
    extra = 0
    show_change_link = True


@admin.register(Category)

class AdminCategory(admin.ModelAdmin):
   
    list_display = ["image_icon","name","description"]
    
    # readonly_fields = ["image_tag","image_icon"]
    inlines=[ImageInline]
   
   


