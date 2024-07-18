from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.location.forms import StoreImageFormSet, StoreForm, AreaForm, AisleForm, UprightForm, AssignItemForm
from apps.location.models import Store, Area, Aisle, Upright, AssignItem
from apps.product.models import Product
from apps.user.models import User


# Create your views here.
def location(request):
    return HttpResponse('Hello Location App')


class ListLocationView(TemplateView):
    template_name = 'location/list.html'



class ListCustomerViewJson( AjayDatatableView):
    model = User
    columns = ['first_name', 'last_name', 'email', 'actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.filter(user_type='customer')

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse_lazy('admin-location-detail', kwargs={'customer_id': row.pk}))

            return detail_action
        else:
            return super(ListCustomerViewJson, self).render_column(row, column)


# Store Views Classes


class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'location/store_form.html'
    # success_url = reverse_lazy('admin-location-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_id'] = self.kwargs['customer_id']
        return context

    def form_valid(self, form):
        store = form.save(commit=False)
        customer_id = self.kwargs['customer_id']
        customer = get_object_or_404(User, id=customer_id)
        store.customer = customer
        store.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('admin-location-detail', kwargs={'customer_id': self.kwargs['customer_id']})


class StoreTemplateView(TemplateView):
    template_name = 'location/storetemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs.get('customer_id')
        context['customer'] = get_object_or_404(User, id=customer_id)
        context['stores'] = Store.objects.filter(customer_id=customer_id)
        return context


class StoreListViewAjax(AjayDatatableView):
    model = Store
    columns = ['customer_id','id','name','actions']

    def get_initial_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return self.model.objects.filter(customer_id=customer_id)

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse_lazy('admin-location-area-detail', kwargs={'store_id': row.pk}))

            return detail_action
        else:
            return super(StoreListViewAjax, self).render_column(row, column)



# Area Views Classes


class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'location/area_form.html'
    # success_url = reverse_lazy('admin-location-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store_id'] = self.kwargs['store_id']
        return context

    def form_valid(self, form):
        area = form.save(commit=False)
        store_id = self.kwargs['store_id']
        store = get_object_or_404(Store, id=store_id)
        area.store = store
        area.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('admin-location-area-detail',kwargs={'store_id':self.kwargs['store_id']})


class AreaTemplateView(TemplateView):
    template_name = 'location/areatemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store_id = self.kwargs.get('store_id')
        context['store'] = get_object_or_404(Store, id=store_id)
        context['areas'] = Area.objects.filter(store_id=store_id)
        return context


class ListLocationAreaViewJson(AjayDatatableView):
    model = Area
    columns = ['store_id','id','area_name','actions']

    def get_initial_queryset(self):
        store_id = self.kwargs.get('store_id')
        return self.model.objects.filter(store_id=store_id)

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse_lazy('admin-location-aisle-detail', kwargs={'area_id': row.pk}))

            return detail_action
        else:
            return super(ListLocationAreaViewJson, self).render_column(row, column)



# Aisle Views Classes

class AisleTemplateView(TemplateView):
    template_name = 'location/aisletemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_id = self.kwargs.get('area_id')
        context['area'] = get_object_or_404(Area, id=area_id)
        return context



class AisleCreateView(CreateView):
    model = Aisle
    form_class = AisleForm
    template_name = 'location/aisle_form.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['area_id']=self.kwargs['area_id']
        return context

    def form_valid(self, form):
        aisle = form.save(commit=False)
        area_id = self.kwargs['area_id']
        area = get_object_or_404(Area, id=area_id)
        aisle.area = area
        aisle.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('admin-location-aisle-detail',kwargs={'area_id':self.kwargs['area_id']})


class AisleListViewJson(AjayDatatableView):
    model = Aisle
    columns = ['area_id','id','aisle_name','actions']

    def get_initial_queryset(self):
        area_id = self.kwargs.get('area_id')
        return self.model.objects.filter(area_id=area_id)

    def render_column(self, row, column):
        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse_lazy('admin-location-upright-detail', kwargs={'aisle_id':row.pk}))

            return detail_action
        else:
            return super(AisleListViewJson, self).render_column(row, column)


# Upright Views Classes

class UprightTemplateView(TemplateView):
    template_name = 'location/uprighttemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aisle_id = self.kwargs.get('aisle_id')
        context['aisle'] = get_object_or_404(Aisle, id=aisle_id)
        return context


class UprightCreateView(CreateView):
    model = Upright
    form_class = UprightForm
    template_name = 'location/upright_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aisle_id']=self.kwargs['aisle_id']
        return context

    def form_valid(self, form):
        upright = form.save(commit=False)
        aisle_id = self.kwargs['aisle_id']
        aisle = get_object_or_404(Aisle, id=aisle_id)
        upright.aisle = aisle
        upright.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('admin-location-upright-detail',kwargs={'aisle_id':self.kwargs['aisle_id']})

class UprightListViewJson(AjayDatatableView):
    model = Upright
    columns = ['aisle_id', 'id', 'upright_name', 'actions']

    def get_initial_queryset(self):
        aisle_id = self.kwargs.get('aisle_id')
        return self.model.objects.filter(aisle_id=aisle_id)

    def render_column(self, row, column):
        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse_lazy('admin-location-assign_item-detail', kwargs={'upright_id': row.pk}))
            return detail_action
        else:
            return super(UprightListViewJson, self).render_column(row, column)


# AssignItem Views Classes

class AssignItemTemplateView(TemplateView):
    template_name = 'location/assign_item_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upright_id = self.kwargs.get('upright_id')
        context['upright'] = get_object_or_404(Upright, id=upright_id)
        return context


class AssignItemCreateView(CreateView):
    model = AssignItem
    form_class = AssignItemForm
    template_name = 'location/assign_item_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upright_id'] = self.kwargs['upright_id']
        print('/////////////////')
        print(context)
        return context

    def form_valid(self, form):
        assign_item = form.save(commit=False)
        upright_id = self.kwargs['upright_id']
        upright = get_object_or_404(Upright, id=upright_id)
        print(upright)
        print('////////////////////////////////')
        assign_item.upright = upright
        assign_item.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        print(form)
        print('////////////////////////////')
        if form.is_valid():
            print("djhdjhdjhdjdhjdhdj")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('admin-location-assign_item-detail', kwargs={'upright_id': self.kwargs['upright_id']})

class AssignItemListViewAjax(AjayDatatableView):
    model = AssignItem
    columns = ['upright_id', 'id', 'upc', 'sku', 'barcode_number', 'quantity']

    def get_initial_queryset(self):
        upright_id = self.kwargs.get('upright_id')
        return self.model.objects.filter(upright_id=upright_id)



