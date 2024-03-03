from django.shortcuts import render
from .models import purchase

# Create your views here.
def PurchaseDetail(request):
    context = {
        't':'Purchase Management',
        'purchase':purchase.objects.all()
    }
    return render(request, 'purchase.html',context)