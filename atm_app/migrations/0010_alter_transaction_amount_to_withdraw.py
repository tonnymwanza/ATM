# Generated by Django 4.1 on 2024-09-27 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm_app', '0009_alter_transaction_amount_to_withdraw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount_to_withdraw',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
