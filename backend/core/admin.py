from django.contrib import admin
from .models import Category, Product, ProductImage, ContactMessage


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4
    max_num = 4

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ContactMessage)
