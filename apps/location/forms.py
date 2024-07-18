from django import forms
from django.forms import inlineformset_factory

from apps.location.models import Store, StoreImage, Area, Aisle, Upright, AssignItem


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']

class StoreImageForm(forms.ModelForm):
    class Meta:
        model = StoreImage
        fields = []

StoreImageFormSet = inlineformset_factory(
    Store , StoreImage , form=StoreImageForm,extra=1,can_delete=True
)

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields =['area_name']


class AisleForm(forms.ModelForm):
    class Meta:
        model = Aisle
        fields =['aisle_name']

class UprightForm(forms.ModelForm):
    class Meta:
        model = Upright
        fields =['upright_name']


class AssignItemForm(forms.ModelForm):
    class Meta:
        model = AssignItem
        fields = ['upc', 'sku', 'barcode_number', 'quantity']