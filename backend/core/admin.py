from django.contrib import admin
from .models import Category, Product, ProductImage, ContactMessage
from django.utils.html import format_html


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4
    max_num = 4
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No image"
    image_preview.short_description = "Preview"

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_name', 'image_preview']

    def image_name(self, obj):
        return obj.image.public_id if hasattr(obj.image, 'public_id') else 'No name'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No image"
    image_preview.short_description = "Preview"
    
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ContactMessage)
