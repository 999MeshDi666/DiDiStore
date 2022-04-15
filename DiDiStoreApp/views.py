from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'DiDiStoreApp/index.html',{'title': 'Главная'})

def account(request):
    return render(request, 'DiDiStoreApp/account.html', {'title': 'Личный кабинет'})

def desired(request):
    return render(request, 'DiDiStoreApp/desired.html', {'title': 'Желаемое'})

def details(request):
    return render(request, 'DiDiStoreApp/details.html', {'title': 'Подробнее'})