# Generated by Django 5.0.6 on 2024-06-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_alter_trade_strategy'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='strategy_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]