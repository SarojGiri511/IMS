from django.shortcuts import render
from .models import vendors
from .form import vendorsForm


# Create your views here.
def vendorHome(request):
    form = vendorsForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = vendors.objects.get(id=pk)
                items = vendorsForm(request.POST,instance=item)
            else: 
                items = vendorsForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = vendors.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = vendors.objects.get(id=pk)
            form = vendorsForm(instance=item)   


    context ={
        'forms': form, 
        't':'Vendor Management',
        'vendor':vendors.objects.all()
    }
    return render(request, 'vendor.html',context)