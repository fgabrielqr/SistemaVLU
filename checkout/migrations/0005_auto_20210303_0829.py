# Generated by Django 3.1.7 on 2021-03-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210209_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('paypal', 'Paypal')], default='deposit', max_length=20, verbose_name='Opção de Pagamento'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Concluída'), (1, 'Aguardando Pagamento'), (2, 'Cancelada')], default=0, verbose_name='Situação'),
        ),
    ]
