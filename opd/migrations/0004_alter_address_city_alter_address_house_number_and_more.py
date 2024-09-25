# Generated by Django 5.1.1 on 2024-09-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0003_inventory_address_pincode_inventory_items_opd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=200, verbose_name='City Name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='house_number',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='House Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=200, verbose_name='State Name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=200, verbose_name='Street Name'),
        ),
        migrations.AlterField(
            model_name='inventory_items',
            name='item_name',
            field=models.CharField(max_length=255, verbose_name='Name of Item'),
        ),
        migrations.AlterField(
            model_name='inventory_items',
            name='item_price',
            field=models.FloatField(default=0, verbose_name='Price of Item'),
        ),
        migrations.AlterField(
            model_name='inventory_items',
            name='item_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantity of Item'),
        ),
        migrations.AlterField(
            model_name='opd',
            name='active_patient',
            field=models.PositiveIntegerField(default=0, verbose_name='No. of Active_Patient'),
        ),
        migrations.AlterField(
            model_name='opd',
            name='max_patient_capacity',
            field=models.PositiveIntegerField(default=0, verbose_name='Maximum Patient Capacity'),
        ),
        migrations.AlterField(
            model_name='opd',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name of OPD'),
        ),
        migrations.AlterField(
            model_name='opd',
            name='no_of_appointment',
            field=models.PositiveIntegerField(default=0, verbose_name='No. of Appointment'),
        ),
    ]