from django.test import TestCase

from . models import Deposit
from . models import Withdraw
from . models import Balance
# Create your tests here.

# testing the Deposit model
class TestDeposit(TestCase):

    def setUp(self):
        self.deposit = Deposit.objects.create(
            amount=20
        )

    def test_deposit(self):
        self.deposit = Deposit.objects.filter(amount__exact=20)
        self.assertTrue(self.deposit)
        self.deposit2 = Deposit.objects.get(id=1)
        self.assertEqual(self.deposit2.amount, 20)

# testing the withdraw model
class TestWithdraw(TestCase):

    def setUp(self):
        self.withdraw = Withdraw.objects.create(
            amount = 1000
        )

    def test_withdraw(self):
        self.assertEqual(self.withdraw.amount, 1000)

# testing the balance model
class TestBalance(TestCase):

    def setUp(self):
        self.balance = Balance.objects.create(
            amount = 2000
        )

    def test_balance(self):
        self.assertEqual(self.balance.amount, 2000)