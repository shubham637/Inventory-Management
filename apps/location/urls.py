from django.urls import path

from apps.location import views
from apps.location.views import ListLocationView, ListCustomerViewJson, StoreCreateView, StoreTemplateView, \
    StoreListViewAjax, AreaTemplateView, AreaCreateView, ListLocationAreaViewJson, AisleTemplateView, AisleCreateView, \
    AisleListViewJson, UprightTemplateView, UprightCreateView, UprightListViewJson, AssignItemTemplateView, \
    AssignItemListViewAjax, AssignItemCreateView

urlpatterns =[
    path('location/',views.location,name='test-location'),
    path('admin/location/',ListLocationView.as_view(),name='admin-location-list'),
    path('admin/location/list/ajax', ListCustomerViewJson.as_view(), name='admin-Lcustomer-list-ajax'),
    # Store related Paths
    path('admin/location/store/list/ajax/<int:customer_id>/', StoreListViewAjax.as_view(), name='admin-store-list-ajax'),
    path('store/add/<int:customer_id>/', StoreCreateView.as_view(), name='store-add'),
    path('admin/location/detail/<int:customer_id>/', StoreTemplateView.as_view(), name='admin-location-detail'),
    # Area related Paths
    path('admin/location/area/create/<int:store_id>/',AreaCreateView.as_view(),name='admin-location-area-create'),
    path('admin/location/area/ajax/<int:store_id>/', ListLocationAreaViewJson.as_view(), name='admin-location-area-ajax'),
    path('admin/location/area/detail/<int:store_id>/', AreaTemplateView.as_view(), name='admin-location-area-detail'),
    # Aisle related Paths
    path('admin/location/aisle/detail/<int:area_id>',AisleTemplateView.as_view(),name='admin-location-aisle-detail'),
    path('admin/location/aisle/create/<int:area_id>',AisleCreateView.as_view(),name='admin-location-aisle-create'),
    path('admin/location/aisle/list/ajax/<int:area_id>',AisleListViewJson.as_view(),name='admin-location-aisle-list-ajax'),
    # Upright related Paths
    path('admin/location/upright/detail/<int:aisle_id>',UprightTemplateView.as_view(),name='admin-location-upright-detail'),
    path('admin/location/upright/create/<int:aisle_id>',UprightCreateView.as_view(),name='admin-location-upright-create'),
    path('admin/location/upright/list/ajax/<int:aisle_id>',UprightListViewJson.as_view(),name='admin-location-upright-list-ajax'),
    # Assign related Pahts
    path('admin/location/assign_item/detail/<int:upright_id>',AssignItemTemplateView.as_view(),name='admin-location-assign_item-detail'),
    path('admin/location/assign_item/create/<int:upright_id>',AssignItemCreateView.as_view(),name='admin-location-assign_item-create'),
    path('admin/location/assign_item/list/ajax/<int:upright_id>',AssignItemListViewAjax.as_view(),name='admin-location-assign_item-list-ajax'),

]