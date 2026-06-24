from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Color, Size, Product, ProductPicture

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','description',]
    search_fields = ['title',]

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','name',]
    search_fields = ['name',]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id','size',]
    search_fields = ['size',]

class ProductPictureInLine(admin.TabularInline):
    model = ProductPicture
    extra = 3   

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'product_picture',
        'category',
        'inventory',
        'price',
        'created_at',
    ]
    search_fields = [
        'title',
    ]
    list_filter = [
        'category',
        'created_at',
    ]
    list_editable = [
        'inventory',
        'price',
    ]
    list_per_page = 10
    inlines = [ProductPictureInLine,]

    def product_picture(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px;" />',
                obj.image.url
            )
        return "-"
    
    product_picture.short_description = "Image"
    
