from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'balance']


class OperationSerializer(serializers.Serializer):
    operationType = serializers.ChoiceField(choices=["DEPOSIT", "WITHDRAW"])
    amount = serializers.FloatField()
