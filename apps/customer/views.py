from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView , TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.customer.forms import CreateCustomerForm
from apps.user.models import User


# Create your views here.
class CreateCustomerView(CreateView,SuccessMessageMixin):
    model = User
    form_class = CreateCustomerForm
    template_name = 'customer/customer/form.html'
    success_message = 'Customer Created Successfully'
    success_url = reverse_lazy('admin-customer-list')

    def form_valid(self, form):
        user = form.save(commit=False)  # Don't save to the database yet
        user.user_type = 'customer'
        user.save()  # Save the user to the database
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListCustomerView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'customer/customer/list.html'


class ListCustomerViewJson(AdminRequiredMixin, AjayDatatableView):
    model = User
    columns = ['first_name', 'last_name', 'email', 'is_active', 'actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.filter(user_type='customer')

    def render_column(self, row, column):
        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-user-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-user-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-user-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ListCustomerViewJson, self).render_column(row, column)