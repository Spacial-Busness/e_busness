# Generated by Django 5.0 on 2024-01-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busness_e_commerce_app', '0003_account_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
