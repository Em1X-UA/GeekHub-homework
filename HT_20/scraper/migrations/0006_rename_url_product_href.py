# Generated by Django 4.1.5 on 2023-01-16 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_rename_href_product_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='URL',
            new_name='href',
        ),
    ]
