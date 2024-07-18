from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, DetailView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.product.forms import ProductForm, ProductImageFormSet
from apps.product.models import Product, ProductImage


# Create your views here.
def index(request):
    return HttpResponse('Hello Product App')


class ProductAdd(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('admin-product-list')  # Update with your actual success URL

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ProductImageFormSet(self.request.POST, self.request.FILES)
        else:
            data['formset'] = ProductImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ListProductView(TemplateView):
    template_name = 'product/list.html'


class ListProductViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Product
    columns = ['name','title','sku', 'upc_number',"actions"]
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.all()

    def render_column(self, row, column):

        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'



        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-product-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-product-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-product-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action + detail_action
        else:
            return super(ListProductViewJson, self).render_column(row,column)

class UpdateProductView( SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'
    success_message = "User updated successfully"
    success_url = reverse_lazy('product-add-list')



class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = context['images'] = self.object.images.all()
        return context

class DeleteProductView(AdminRequiredMixin, DeleteView):
    model = Product

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)