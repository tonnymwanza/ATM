from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import redirect
# Create your views here.

# home page view
class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
    
# the view to render the withdraw page
class WithdrawView(LoginRequiredMixin, View):
    login_url = 'login_view'

    def get(self, request):
        return render(request, 'withdraw.html')

# the view to render the deposit page
class DepositView(LoginRequiredMixin, View):
    login_url = 'login_view'

    def get(self, request):
        return render(request, 'deposit.html')
    
# the view to render the balance page
class BalanceView(LoginRequiredMixin, View):
    login_url = 'login_view'

    def get(self, request):
        return render(request, 'balance.html')
    
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