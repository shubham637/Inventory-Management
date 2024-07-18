from django.urls import path, include
from rest_framework import routers
from apps.item.item_rest_api.views import ItemApiViewSet

router = routers.DefaultRouter()
router.register(r'item_rest_api', ItemApiViewSet)

urlpatterns =[
    path('api/v2/', include(router.urls)),

]

