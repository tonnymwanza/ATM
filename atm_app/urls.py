from . views import HomeView
from django.urls import path
# my urls

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
]

