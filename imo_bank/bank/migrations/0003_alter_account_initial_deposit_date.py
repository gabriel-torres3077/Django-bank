# Generated by Django 4.1.7 on 2023-03-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_remove_account_birth_date_remove_account_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='initial_deposit_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
