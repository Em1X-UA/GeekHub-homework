# Generated by Django 4.1.5 on 2023-01-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(default='n/a', max_length=15)),
                ('title', models.CharField(default='n/a', max_length=255)),
                ('old_price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('URL', models.URLField(default='n/a')),
                ('brand', models.CharField(default='n/a', max_length=50)),
                ('category', models.CharField(default='n/a', max_length=100)),
            ],
        ),
    ]