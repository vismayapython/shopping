# Generated by Django 2.2 on 2022-01-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220105_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]