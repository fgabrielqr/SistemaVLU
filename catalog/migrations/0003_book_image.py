# Generated by Django 3.1.6 on 2021-02-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210203_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books', verbose_name='Imagem'),
        ),
    ]
