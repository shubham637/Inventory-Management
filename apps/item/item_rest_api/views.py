from rest_framework import viewsets
from apps.item.item_rest_api.serializers import ItemSerializer
from apps.item.models import Item


class ItemApiViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer