# Generated by Django 5.1 on 2024-09-25 17:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
    ]