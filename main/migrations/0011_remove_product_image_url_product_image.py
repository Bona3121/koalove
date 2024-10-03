# Generated by Django 5.1.1 on 2024-10-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_remove_product_image_product_image_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image_url",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="products_images/"
            ),
        ),
    ]
