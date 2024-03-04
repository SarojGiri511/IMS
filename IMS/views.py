from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'title':'Inventory Management System'
    }
    return render(request, 'home.html',context)

def sign(request):
    return render(request, 'sign.html')