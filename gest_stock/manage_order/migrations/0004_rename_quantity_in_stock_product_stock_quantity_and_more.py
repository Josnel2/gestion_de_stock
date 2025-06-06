# Generated by Django 5.1.2 on 2024-12-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_order', '0003_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity_in_stock',
            new_name='stock_quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='min_threshold',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
