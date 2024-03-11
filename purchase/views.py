from django.shortcuts import render
from .models import purchase
from .forms import PurchaseForm


# Create your views here.
def purchaseHome(request):
    form = PurchaseForm()
    if request.method == 'POST':
        if 'save' in request.POST:
            purchase_add_edit(request)            
        elif 'delete' in request.POST:
            purchase_delete(request)
        elif 'edit' in request.POST:
            form = purchase_edit(request)

    context = {
        'forms': form,
        'title':'Purchase',
        'purchases':purchase.objects.all()
    }
    
    return render(request,'purchase.html', context)


def purchase_add_edit(request):
    if request.POST.get('save'):
        pk = request.POST.get('save')
        item = purchase.objects.get(id=pk)
        items = PurchaseForm(request.POST, request.FILES, instance=item)
    else: 
        items = PurchaseForm(request.POST, request.FILES)
    if items.is_valid:
        items.save()
        
    else:
       return 'Error During Validation'


def purchase_delete(request):
    pk = request.POST.get('delete')
    item = purchase.objects.filter(id=pk)
    item.delete()


def purchase_edit(request):
    pk = request.POST.get('edit')
    item = purchase.objects.get(id=pk)
    return PurchaseForm(instance=item)   



