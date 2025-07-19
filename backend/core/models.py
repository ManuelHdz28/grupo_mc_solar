from django.db import models
import os
from cloudinary.models import CloudinaryField


def upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    return f'product_images/{name}{ext.lower()}'


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')  # ✅ Esto guarda en Cloudinary
    
    def __str__(self):
        return f"{self.product.name} - {self.image.public_id if hasattr(self.image, 'public_id') else 'sin imagen'}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.email} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"