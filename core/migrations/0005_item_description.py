# Generated by Django 5.0.6 on 2024-05-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='test description'),
            preserve_default=False,
        ),
    ]
