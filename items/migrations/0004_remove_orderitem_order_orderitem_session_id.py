# Generated by Django 4.2.7 on 2023-12-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_order_items_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='session_id',
            field=models.CharField(default=2, max_length=32, unique=True),
            preserve_default=False,
        ),
    ]
