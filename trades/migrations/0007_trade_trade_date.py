# Generated by Django 5.0.6 on 2024-06-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0006_trade_strategy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='trade_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
