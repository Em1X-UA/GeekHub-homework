# Generated by Django 4.1.5 on 2023-01-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_item_id', models.IntegerField(max_length=6)),
                ('item_qty', models.IntegerField(default=1, max_length=2)),
            ],
        ),
    ]