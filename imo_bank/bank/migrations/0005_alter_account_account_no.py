# Generated by Django 4.1.7 on 2023-03-08 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_account_initial_deposit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]