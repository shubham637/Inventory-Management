# Generated by Django 3.2 on 2024-07-05 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
