from django.shortcuts import render
from .models import Inventory




# Create your views here.
def InventoryHome(request):
    context ={
        't':'Inventory management',
        'Inventory':Inventory.objects.all()

    }
    return render(request, 'inventory.html',context)