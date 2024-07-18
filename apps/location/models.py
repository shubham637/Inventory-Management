from django.db import models

from apps.user.models import User


# Create your models here.
class Store(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='name',null=True)
    name = models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)

class StoreImage(models.Model):
    image=models.ImageField(upload_to='image/',null=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name='images')


class Area(models.Model):
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name='area',null=True)
    area_name = models.CharField(max_length=50)

class Aisle(models.Model):
    area=models.ForeignKey(Area,on_delete=models.CASCADE,related_name='aisle',null=True)
    aisle_name = models.CharField(max_length=50)

class Upright(models.Model):
    aisle=models.ForeignKey(Aisle,on_delete=models.CASCADE,related_name='upright',null=True)
    upright_name = models.CharField(max_length=50)


class AssignItem(models.Model):
    upright = models.ForeignKey(Upright,on_delete=models.CASCADE,related_name='assign_item',null=True)
    upc = models.CharField(max_length=20)
    sku = models.CharField(max_length=20)
    barcode_number = models.IntegerField(max_length=15,null=True)
    quantity = models.IntegerField(max_length=10,null=True)