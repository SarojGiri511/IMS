from django.shortcuts import render
from .models import Purchase
from .forms import PurchaseForm


# Create your views here.
def PurchaseHome(request):
    message = 'success'
    form = PurchaseForm()
    if request.method == 'POST':
        if 'save' in request.POST:
            Purchase_add_edit(request)            
        elif 'delete' in request.POST:
            Purchase_delete(request)
        elif 'edit' in request.POST:
            form = Purchase_edit(request)

    context = {
        'forms': form,
        'title':'Purchase',
        'Purchases':Purchase.objects.all(),
        'message':message
    }
    
    return render(request,'Purchase.html', context)


def Purchase_add_edit(request):
    if request.POST.get('save'):
        pk = request.POST.get('save')
        item = Purchase.objects.get(id=pk)
        items = PurchaseForm(request.POST, request.FILES, instance=item)
    else: 
        items = PurchaseForm(request.POST, request.FILES)
    if items.is_valid:
        items.save()
    else:
       message =  'Error During Validation'


def Purchase_delete(request):
    pk = request.POST.get('delete')
    item = Purchase.objects.filter(id=pk)
    item.delete()


def Purchase_edit(request):
    pk = request.POST.get('edit')
    item = Purchase.objects.get(id=pk)
    return PurchaseForm(instance=item)   

def PurchaseAdd(request):
 
    context = {
        'submit_url':'purchase',
        'forms':  PurchaseForm(), 
    }
    return render(request, 'add_new.html', context)

