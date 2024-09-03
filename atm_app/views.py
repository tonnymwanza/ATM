from django.shortcuts import render
from django.views import View
# Create your views here.

# home page view
class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
    
# the view to render the withdraw page
class WithdrawView(View):

    def get(self, request):
        return render(request, 'withdraw.html')

# the view to render the deposit page
class DepositView(View):

    def get(self, request):
        return render(request, 'deposit.html')
    
# the view to render the balance page
class BalanceView(View):

    def get(self, request):
        return render(request, 'balance.html')