# Generated by Django 4.1.5 on 2023-01-16 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='href',
            new_name='URL',
        ),
    ]