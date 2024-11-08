# Generated by Django 5.1.2 on 2024-11-04 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.product_details'),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='images',
            field=models.FileField(upload_to=None),
        ),
    ]
