from django.db import models
from django.utils import timezone


class Trade(models.Model):
    INSTRUMENT_CHOICES = [
        ('bonds', 'Bonds'),
        ('cds', 'CDS'),
        ('futures', 'Futures'),
        ('fx', 'FX'),
    ]

    STRATEGY_CHOICES = [
        ('Active Short', 'Active Short'),
        ('RelVal', 'RelVal'),
        ('SLBs', 'SLBs'),
        ('Curves', 'Curves'),
        ('Use of proceeds', 'Use of proceeds'),
        ('Hedge', 'Hedge'),
    ]
    
    timestamp = models.DateTimeField(auto_now_add=True)
    trade_date = models.DateField(null=True, blank=True)
    trade_id = models.AutoField(primary_key=True)
    security_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    comment = models.TextField(max_length=150)
    strategy = models.CharField(max_length=50, choices=STRATEGY_CHOICES)
    strategy_id = models.CharField(max_length=100, null=True, blank=True)
    instrument_type = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    spread = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notional = models.DecimalField(max_digits=10, decimal_places=2)
    direction = models.CharField(max_length=4)
    no_of_contracts = models.IntegerField(null=True, blank=True)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.security_id

