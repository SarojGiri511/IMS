from django.shortcuts import render
from .models import customer
from .forms import CustomerForm


# Create your views here.
def customerhome(request):
    form = CustomerForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = customer.objects.get(id=pk)
                items = CustomerForm(request.POST,instance=item)
            else: 
                items = CustomerForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = customer.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = customer.objects.get(id=pk)
            form = CustomerForm(instance=item)   


    context = {
        'forms': form, 
        't':'Customer Management',
        'customer':customer.objects.all()



    }
    return render(request,'customer.html',context)