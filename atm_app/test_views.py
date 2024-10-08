from django.urls import reverse
from django.test import TestCase

# testing the views
# testing the view that renders the home page
class TestHomeView(TestCase):

    def test_home_view(self):
        self.response = self.client.get(reverse('home'))
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertTemplateNotUsed(self.response, 'index.html')

# testing the view that renders the withdraw page
class TestWithdraw(TestCase):

    def test_withdraw_view(self):
        self.response = self.client.get(reverse('withdraw'))
        self.assertTemplateNotUsed(self.response, 'home.html')
        self.assertTemplateUsed(self.response, 'withdraw.html')

# testing the view that renders the deposit page
class TestDeposit(TestCase):

    def test_deposit_view(self):
        self.response = self.client.get(reverse('deposit'))
        self.assertTemplateNotUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'deposit.html')

# testing the view that renders the balance page
class TestBalance(TestCase):

    def test_balance_view(self):
        self.response = self.client.get(reverse('balance'))
        self.assertTemplateNotUsed(self.response, 'home.html')
        self.assertTemplateUsed(self.response, 'balance.html')

# testing the view that shows the success message after perfoming a withdrawal
class TestWithdrawSuccessView(TestCase):

    def test_withdraw_success_view(self):
        self.response = self.client.get(reverse('withdraw_success_view'))
        self.assertTemplateNotUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'withdraw_success.html')
        self.assertEqual(self.response.status_code, 200)

# testing the view that renders the success message after depositing
class TestDepositSuccessView(TestCase):

    def test(self):
        self.response = self.client.get(reverse('deposit_success_view'))
        self.assertTemplateNotUsed(self.response, 'index.html')
        self.assertTemplateUsed(self.response, 'deposit_success.html')
        self.assertEqual(self.response.status_code, 200)