# Generated by Django 2.2 on 2022-01-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220111_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='available',
            field=models.BooleanField(),
        ),
    ]
