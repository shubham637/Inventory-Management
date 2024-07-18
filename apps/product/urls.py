from django.urls import path, include

from apps.product import views
from apps.product.views import ProductAdd, ListProductView, ListProductViewJson, UpdateProductView, DeleteProductView, \
    ProductDetailView

urlpatterns = [
    path('product_api/',include('apps.product.product_rest_api.urls')),

    path('index', views.index,name='test'),
    path('productAdd',ProductAdd.as_view(),name='product-add'),
    path('admin/product/', ListProductView.as_view(), name='admin-product-list'),

    path('admin/product/list/ajax', ListProductViewJson.as_view(), name='admin-product-list-ajax'),
    path('admin/product/edit/<int:pk>', UpdateProductView.as_view(), name='admin-product-edit'),
    path('admin/product/detail/<int:pk>', ProductDetailView.as_view(), name='admin-product-detail'),
    path('admin/product/delete/<int:pk>', DeleteProductView.as_view(), name='admin-product-delete'),

]