from django.test import TestCase

from . models import Transaction

# my tests

# testing the Transaction model
class TransactionTestCase(TestCase):

    def setUp(self):
        self.transaction = Transaction.objects.create(
            amount_to_deposit=1000,
            amount_to_withdraw=500,
            check_balance=1500
        )

    def test_transaction(self):
        self.assertEqual(self.transaction.amount_to_deposit, 1000)
        self.assertEqual(self.transaction.amount_to_withdraw, 500)
        self.assertEqual(self.transaction.check_balance, 1500)
        self.assertTrue(self.transaction)