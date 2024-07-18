from rest_framework import viewsets

from apps.product.models import Product
from apps.product.product_rest_api.serializers import ProductSerializer


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer