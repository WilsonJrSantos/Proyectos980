# Generated by Django 4.0a1 on 2021-10-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_product_is_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
