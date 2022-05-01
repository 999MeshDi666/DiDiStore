from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('account/', account, name = 'account'),
    path('desired/', desired, name = 'desired'),
    path('details/', details, name = 'details'),
    path('payments/', payments, name = 'payments'),
]
