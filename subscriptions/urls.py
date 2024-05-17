from django.urls import path
from .views import ActiveSubscriptionView, GetTransactionHistory, InsertTransaction

urlpatterns = [
    path('active/', ActiveSubscriptionView.as_view(), name='active-subscription'),
    path('history/', GetTransactionHistory.as_view(), name='transaction-history'),
    path('buy/', InsertTransaction.as_view(), name='buy-subscription')
]
