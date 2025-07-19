from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ContactMessageViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'messages', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Añadir esto solo si DEBUG está en True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)