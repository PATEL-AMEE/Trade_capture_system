from django import forms
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['instrument_type', 'security_id', 'trade_date', 'notional', 'no_of_contracts', 'price', 'comment', 'spread', 'strategy','direction']
        widgets = {
            'instrument_type': forms.RadioSelect(choices=Trade.INSTRUMENT_CHOICES, attrs={'id': 'instrument_type'}),
            'strategy': forms.Select(choices=Trade.STRATEGY_CHOICES, attrs={'id': 'strategy'}),
            'trade_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'id': 'price'}),
            'spread': forms.NumberInput(attrs={'id': 'spread'}),
            'notional': forms.NumberInput(attrs={'id': 'notional'}),
            'no_of_contracts': forms.NumberInput(attrs={'id': 'no_of_contracts'}),
            'direction': forms.Select(choices=[('Buy', 'Buy'), ('Sell', 'Sell')], attrs={'id': 'direction'}),
        }