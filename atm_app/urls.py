from . views import HomeView
from django.urls import path
from . import views

from . views import WithdrawSuccessView
from . views import WithdrawView
from . views import BalanceView
from . views import DepositView
from . views import DepositSuccessView
from . views import WithdrawWarningView
# my urls

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('withdraw', WithdrawView.as_view(), name='withdraw'),
    path('balance', BalanceView.as_view(), name='balance'),
    path('deposit', DepositView.as_view(), name='deposit'),
    path('login_view', views.login_view, name='login_view'),
    path('registration_view', views.registration_view, name='registration_view'),
    path('withdraw_success_view', WithdrawSuccessView.as_view(), name='withdraw_success_view'),
    path('deposit_success_view', DepositSuccessView.as_view(), name='deposit_success_view'),
    path('withdraw_warning_view', WithdrawWarningView.as_view(), name='withdraw_warning_view'),
]

