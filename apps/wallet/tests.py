import uuid
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Wallet


class WalletAPITests(APITestCase):

    def setUp(self):
        self.wallet = Wallet.objects.create(balance=100)

    def test_perform_deposit(self):
        response = self.client.post(f'/api/v1/wallets/{self.wallet.id}/operation/', {
            'operationType': 'DEPOSIT',
            'amount': 50
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK, "Expected status code 200 for deposit operation")
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, 150, "Wallet balance should be updated to 150 after deposit")

    def test_perform_withdraw(self):
        response = self.client.post(f'/api/v1/wallets/{self.wallet.id}/operation/', {
            'operationType': 'WITHDRAW',
            'amount': 50
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK, "Expected status code 200 for withdraw operation")
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, 50, "Wallet balance should be updated to 50 after withdrawal")

    def test_withdraw_insufficient_funds(self):
        response = self.client.post(f'/api/v1/wallets/{self.wallet.id}/operation/', {
            'operationType': 'WITHDRAW',
            'amount': 150
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         "Expected status code 400 for insufficient funds")
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"detail": "Insufficient funds"},
                             "Expected error message for insufficient funds")

    def test_get_wallet(self):
        response = self.client.get(f'/api/v1/wallets/{self.wallet.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK, "Expected status code 200 for getting wallet")
        self.assertEqual(response.data['balance'], 100, "Wallet balance should be 100")

    def test_get_wallet_not_found(self):
        non_existent_wallet_id = uuid.uuid4()

        response = self.client.get(f'/api/v1/wallets/{non_existent_wallet_id}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND,
                         "Expected status code 404 for non-existing wallet")
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"detail": "Wallet not found"},
                             "Expected error message for wallet not found")
