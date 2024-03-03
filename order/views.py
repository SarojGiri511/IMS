from django.shortcuts import render
from .models import order



# Create your views here.
def orderHome(request):
    context = {
        't':'Order Management',
        'order':order.objects.all()
    }
    return render(request, 'order.html',context)