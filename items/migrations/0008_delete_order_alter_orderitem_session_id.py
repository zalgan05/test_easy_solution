# Generated by Django 4.2.7 on 2023-12-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_price_currency'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='session_id',
            field=models.CharField(max_length=100),
        ),
    ]
