from django.urls import path, include

from apps.customer.views import CreateCustomerView, ListCustomerView, ListCustomerViewJson



urlpatterns =[
    path('rest_api/', include('apps.customer.rest_api.urls')),
    path('admin/customer/add',CreateCustomerView.as_view(),name='admin-customer-add'),
    path('admin/customer/', ListCustomerView.as_view(), name='admin-customer-list'),
    path('admin/customer/list/ajax', ListCustomerViewJson.as_view(), name='admin-customer-list-ajax'),
]