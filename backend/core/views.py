from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, ContactMessage
from .serializers import CategorySerializer, ProductSerializer, ContactMessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail

# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    
    def perform_create(self, serializer):
        # 1️⃣ Guarda el mensaje en la base de datos
        message = serializer.save()

        # 2️⃣ Envía el correo
        send_mail(
            subject=f"Nuevo mensaje de contacto de {message.name}",
            message=(
                f"Has recibido un nuevo mensaje de contacto:\n\n"
                f"Nombre: {message.name}\n"
                f"Correo electrónico: {message.email}\n\n"
                f"Mensaje:\n{message.message}"
            ),
            from_email=None,  # Usa DEFAULT_FROM_EMAIL
            recipient_list=["tu_correo@gmail.com"],  # 🚨 Cambia esto por tu Gmail
        )