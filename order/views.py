from django.shortcuts import render
from .models import order
from .forms import OrderForm



# Create your views here.
def orderHome(request):
    form = OrderForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = order.objects.get(id=pk)
                items = OrderForm(request.POST,instance=item)
            else: 
                items = OrderForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = order.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = order.objects.get(id=pk)
            form = OrderForm(instance=item)   




    context = {
        'forms': form, 
        't':'Order Management',
        'order':order.objects.all()
    }
    return render(request, 'order.html',context)