from django.shortcuts import render
from .models import Vendors
from .form import VendorsForm


# Create your views here.
def VendorHome(request):
    form = VendorsForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Vendors.objects.get(id=pk)
                items = VendorsForm(request.POST,instance=item)
            else: 
                items = VendorsForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Vendors.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Vendors.objects.get(id=pk)
            form = VendorsForm(instance=item)   


    context ={
        'forms': form, 
        't':'Vendor Management',
        'Vendor':Vendors.objects.all()
    }
    return render(request, 'vendor.html',context)


def VendorAdd(request):
 
    context = {
        'submit_url':'vendor',
        'forms':  VendorsForm(), 
    }
    return render(request, 'add_new.html', context)