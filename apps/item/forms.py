from django import forms
from apps.item.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= ['item_name','sku','upc_number','price','description','image']



class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')