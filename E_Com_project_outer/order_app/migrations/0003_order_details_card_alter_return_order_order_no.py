# Generated by Django 5.1.2 on 2024-11-08 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0002_alter_order_details_order_no_return_order'),
        ('product_app', '0002_product_details_card_alter_product_details_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.product_details'),
        ),
        migrations.AlterField(
            model_name='return_order',
            name='order_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.order_details'),
        ),
    ]
