# Generated by Django 3.2 on 2024-06-25 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_store_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='location.store')),
            ],
        ),
    ]