from django.urls import path
from .views import perform_operation, get_wallet

urlpatterns = [
    path('api/v1/wallets/<str:wallet_id>/operation/', perform_operation),
    path('api/v1/wallets/<str:wallet_id>/', get_wallet),
]