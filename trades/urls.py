from trades import views
from django.urls import include, path

app_name = 'trades'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_trade/', views.add_trade, name='add_trade'),
    path('edit/<int:id>/', views.edit_trade, name='edit_trade'),
    path('delete/<int:id>/', views.delete_trade, name='delete_trade'),
    path('update/', views.update_trades, name='update_trades')
]
