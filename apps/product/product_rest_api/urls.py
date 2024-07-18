from django.urls import path, include
from rest_framework import routers

from apps.product.product_rest_api.views import ProductApiViewSet

router = routers.DefaultRouter()
router.register(r'product_rest_api', ProductApiViewSet)

urlpatterns = [
    path('api/v3/', include(router.urls))
]