from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import redirect
from django.db.models import Sum

from . models import Transaction
from . forms import WithdrawForm
from . forms import DepositForm
from . forms import BalanceForm
# Create your views here.

# home page view
class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
    
# the view to render the withdraw page
class WithdrawView(LoginRequiredMixin,View):
    login_url = 'login_view'
    form = WithdrawForm
    errors = None

    def get(self, request):
        form = WithdrawForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'withdraw.html', context)
    
    def post(self, request):
        form = WithdrawForm(request.POST)
        if form.is_valid():
            withdraw_transaction = Transaction.objects.create(
                amount_to_withdraw = form.cleaned_data['amount_to_withdraw'],
                user = request.user
            )
            return redirect('withdraw_success_view')
        else:
            messages.error(request, 'error sending the information')
            my_errors = form.errors
        context = {
            'my_errors': my_errors
        }
        context
        print('the context data', context)
        return redirect('withdraw')

# the view to render the deposit page
class DepositView(LoginRequiredMixin,View):
    login_url = 'login_view'

    def get(self, request):
        form = DepositForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'deposit.html', context  )
    
    def post(self, request):
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit_transaction = Transaction.objects.create(
                amount_to_deposit = form.cleaned_data['amount_to_deposit'],
                user = request.user
            )
            return redirect('deposit_success_view')
        else:
            messages.error(request, 'error during sending of the message')
        return redirect('deposit')
    
# the view to render the balance page
class BalanceView(LoginRequiredMixin,View):
    login_url = 'login_view'

    def get(self, request):
        the_balance = Transaction.objects.aggregate(your_balance_is=Sum('amount_to_deposit'))
        context = {
            'the_balance': the_balance
        }
        return render(request, 'balance.html', context)
 
    
# the registration view
def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'the username is in use already. find another one')
            else:
                user = User.objects.create_user(username = username, password = password)
                return redirect('login_view')
        else:
            messages.error(request, 'error!!! the passwords dont match')
    return render(request, 'signup.html')

# the login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('home')
        else:
            messages.error(request, 'invalid username or password. check to continue')
    return render(request, 'login.html')

# the view to render the success message after withdrawal
class WithdrawSuccessView(View):

    def get(self, request):
        last_transaction = Transaction.objects.last()
        last_transaction = last_transaction.amount_to_withdraw
        context = {
            'last_transaction': last_transaction
        }
        return render(request, 'withdraw_success.html', context)
    
# the view to show the success message after depositing
class DepositSuccessView(View):
    
    def get(self, request):
        last_transaction = Transaction.objects.last()
        last_transaction = last_transaction.amount_to_deposit
        context = {
            'last_transaction': last_transaction
        }
        return render(request, 'deposit_success.html',context)