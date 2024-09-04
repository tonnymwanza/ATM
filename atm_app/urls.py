from . views import HomeView
from django.urls import path

from . views import WithdrawView
from . views import BalanceView
from . views import DepositView
from . import views
# my urls

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('withdraw', WithdrawView.as_view(), name='withdraw'),
    path('balance', BalanceView.as_view(), name='balance'),
    path('deposit', DepositView.as_view(), name='deposit'),
    path('login_view', views.login_view, name='login_view'),
    path('registration_view', views.registration_view, name='registration_view'),
]

