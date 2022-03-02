from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('account/', account),
    path('desired/', desired, name = 'desired'),
]
