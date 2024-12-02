from django.test import TestCase

from . models import Transaction

# my tests

# testing the Transaction model
class TransactionTestCase(TestCase):

    def setUp(self):
        self.transaction = Transaction.objects.create(
            user_name = 'tinny',
            account_number = 3253,
            balance = 400
        )

    def test_transaction(self):
        self.assertEqual(self.transaction.user_name, 'tinny')
        self.assertEqual(self.transaction.account_number, 3253)
        self.assertEqual(self.transaction.balance, 400)
        self.assertTrue(self.transaction)