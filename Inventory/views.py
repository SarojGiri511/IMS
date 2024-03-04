from django.shortcuts import render
from .models import Inventory
from .forms import InventoryForm




# Create your views here.
def InventoryHome(request):
    form = InventoryForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Inventory.objects.get(id=pk)
                items = InventoryForm(request.POST,instance=item)
            else: 
                items = InventoryForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Inventory.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Inventory.objects.get(id=pk)
            form = InventoryForm(instance=item)   


    context ={
        'forms': form, 
        't':'Inventory management',
        'Inventory':Inventory.objects.all()

    }
    return render(request, 'inventory.html',context)