from typing import Counter
from django.shortcuts import render, redirect, get_object_or_404
from trades.models import Trade
from trades.forms import TradeForm
from datetime import datetime
from django.http import JsonResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

def index(request):
    trades = Trade.objects.filter(is_submitted=False)
    tradeData = Trade.objects.filter()
    # instrumentTypes = [trade.instrument_type for trade in tradeData]

    # trade_price = list(trades.values('price'))
    instrumentTypes = list(trades.values('instrument_type'))
    form = TradeForm()
    return render(request, 'index.html', {'trades': trades, 'form': form,'trade_types': instrumentTypes})

def add_trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TradeForm()
    return render(request, 'trades/add_trade.html', {'form': form})


def edit_trade(request, id):
    trade = get_object_or_404(Trade, trade_id=id)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TradeForm(instance=trade)
    return render(request, 'trades/edit_trade.html', {'form': form})

def delete_trade(request, id):
    trade = get_object_or_404(Trade, trade_id=id)
    if request.method == 'POST':
        trade.delete()
        return redirect('index')
    return render(request, 'trades/delete_trade.html', {'trade': trade})
    

def update_trades(request):
    if request.method == 'POST':
        try:
            with transaction.atomic(): 
                Trade.objects.filter(is_submitted=False).update(is_submitted=True) 
                return JsonResponse({'message': 'Data updated successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def trade_list(request):
    trades = Trade.objects.all()
    static_user_name = "static_user"
    for trade in trades:
        trade.user_name = static_user_name
    return render(request, 'index.html', {'trades': trades})
 
