from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Wallet
from .serializers import OperationSerializer, WalletSerializer

@api_view(['POST'])
def perform_operation(request, wallet_id):
    try:
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(id=wallet_id)
    except Wallet.DoesNotExist:
        return Response({"detail": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = OperationSerializer(data=request.data)
    if serializer.is_valid():
        operation_type = serializer.validated_data['operationType']
        amount = serializer.validated_data['amount']

        if amount < 0:
            return Response({"detail": "Amount must be positive"}, status=status.HTTP_400_BAD_REQUEST)

        if operation_type == "DEPOSIT":
            wallet.balance += amount
        elif operation_type == "WITHDRAW":
            if wallet.balance < amount:
                return Response({"detail": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
            wallet.balance -= amount

        wallet.save()
        return Response(WalletSerializer(wallet).data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_wallet(request, wallet_id):
    try:
        wallet = Wallet.objects.get(id=wallet_id)
        return Response(WalletSerializer(wallet).data)
    except Wallet.DoesNotExist:
        return Response({"detail": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
