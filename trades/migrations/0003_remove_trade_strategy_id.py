# Generated by Django 5.0.6 on 2024-06-08 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_alter_trade_direction_alter_trade_instrument_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='strategy_id',
        ),
    ]