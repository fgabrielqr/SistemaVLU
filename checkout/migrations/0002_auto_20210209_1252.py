# Generated by Django 3.1.6 on 2021-02-09 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210203_1231'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart_key', 'book')},
        ),
    ]
