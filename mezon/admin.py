from django.contrib import admin

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
    
