import csv
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.item.forms import ItemForm, CSVUploadForm
from apps.item.models import Item


# Create your views here.


class ItemAdd(CreateView,SuccessMessageMixin):
    model = Item
    form_class = ItemForm
    template_name = 'item/form.html'
    success_message = 'Item Add Successfully'
    success_url = reverse_lazy('admin-item-list')


class ListItemView(TemplateView):
    template_name = 'item/list.html'

class DetailItemView(TemplateView):
    template_name = 'item/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailItemView, self).get_context_data(**kwargs)
        context['item'] = Item.objects.get(id=kwargs['pk'])
        return context

class UpdateItemView(SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/form.html'
    success_message = "Item updated successfully"
    success_url = reverse_lazy('admin-item-list')

class DeleteItemView(AdminRequiredMixin,DeleteView):
    model = Item

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)
class ListItemViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Item
    columns = ['item_name', 'sku', 'upc_number', 'price', 'description','image',"actions"]
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

        if column == 'image':
            return f'<img src="{row.image.url}" height=50px alt="Sample Image">'

        if column == 'actions':
            # detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
            #     reverse('admin-item-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-item-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-item-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ListItemViewJson, self).render_column(row,column)


#  Upload CSV File Function

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            file_data = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(file_data)
            print(reader)
            headers = reader.fieldnames
            print(f"CSV Headers: {headers}")
            for row in reader:
               try:
                   Item.objects.create(
                       item_name=row['Item_name'],
                       sku=row['SKU'],
                       upc_number=row['UPC_number'],
                       price=row['Price'],
                       description=row['Description'],
                       image=row['image'],
                   )
               except Exception as e:
                   print(f'Error inserting in Row{e}')
        return render(request, 'item/list.html')
    else:
        form = CSVUploadForm()
    return render(request, 'item/uploadCSV.html', {'form': form})
