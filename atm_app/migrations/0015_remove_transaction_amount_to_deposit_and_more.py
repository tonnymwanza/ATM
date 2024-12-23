# Generated by Django 5.0.6 on 2024-12-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm_app', '0014_alter_transaction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount_to_deposit',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='amount_to_withdraw',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='balance_after_withdrawal',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='check_balance',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account_number',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
