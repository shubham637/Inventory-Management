from django.urls import path, include
from rest_framework import routers
from apps.customer.rest_api.views import CustomerApiViewSet

router = routers.DefaultRouter()
router.register(r'customer_rest_api', CustomerApiViewSet)


urlpatterns =[
    path('api/v1/', include(router.urls)),
]

