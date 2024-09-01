from django.test import TestCase

from . models import Deposit
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