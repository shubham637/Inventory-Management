from django.urls import path, include

from . import views
from .views import ItemAdd, ListItemView, ListItemViewJson, DetailItemView, DeleteItemView,UpdateItemView

urlpatterns = [
    path('item_api/',include('apps.item.item_rest_api.urls')),
    path('itemadd/',ItemAdd.as_view(),name='item-add'),
    path('admin/Item', ListItemView.as_view(), name='admin-item-list'),
    path('admin/item/list/ajax', ListItemViewJson.as_view(), name='admin-item-list-ajax'),
    path('admin/item/edit/<int:pk>', UpdateItemView.as_view(), name='admin-item-edit'),
    path('admin/item/delete/<int:pk>', DeleteItemView.as_view(), name='admin-item-delete'),
    # path('admin/item/detail/<int:pk>', DetailItemView.as_view(), name='admin-item-detail'),

#     CSV FILE Upload
    path('upload/', views.upload_csv, name='upload_csv'),
]