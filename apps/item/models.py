from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField('Item Name', max_length=100,blank=True)
    sku = models.CharField('Sku',max_length=10,blank=True)
    upc_number = models.CharField('UPC Number',null=True,max_length=50)
    price = models.IntegerField('price', null=True)
    description = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to ='uploads/',null=True)
