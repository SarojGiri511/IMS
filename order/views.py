from django.shortcuts import render
from .models import Order
from .forms import OrderForm



# Create your views here.
def OrderHome(request):
    form = OrderForm()
   
    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Order.objects.get(id=pk)
                items = OrderForm(request.POST,instance=item)
                if items.is_valid():
                    items.save()
                else:
                    context = {
                                'forms': form, 
                                't':'Order Management',
                                'Order':Order.objects.all(),
                                'message':'Invalid Value Entered'
                            }
                    return render(request, 'order.html',context)
            else: 
                items = OrderForm(request.POST)
                if items.is_valid():
                    items.save()
                else:
                    context = {
                                'forms': form, 
                                't':'Order Management',
                                'order':Order.objects.all(),
                                'message':'Invalid Value Entered'
                            }
                    return render(request, 'order.html',context)

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Order.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Order.objects.get(id=pk)
            form = OrderForm(instance=item)   




    context = {
        'forms': form, 
        't':'Order Management',
        'order':Order.objects.all()
    }
    return render(request, 'order.html',context)

def OrderAdd(request):
 
    context = {
        'submit_url':'Order',
        'forms':  OrderForm(), 
    }
    return render(request, 'add_new.html', context)

