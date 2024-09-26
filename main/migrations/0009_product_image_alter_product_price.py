# Generated by Django 5.1.1 on 2024-09-26 03:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_alter_product_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(),
        ),
    ]