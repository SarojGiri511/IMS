from django.shortcuts import render
from .models import Sales
from .forms import SalesForm




# Create your views here.
def Saleshome(request):
    form = SalesForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Sales.objects.get(id=pk)
                items = SalesForm(request.POST,instance=item)
            else: 
                items = SalesForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Sales.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Sales.objects.get(id=pk)
            form = SalesForm(instance=item)   
    context = {
        'forms': form, 
        't':'Sales Management',
        'Sales':Sales.objects.all()
    }
    return render(request,'sales.html',context)

def SalesAdd(request):
 
    context = {
        'submit_url':'Sales',
        'forms':  SalesForm(), 
    }
    return render(request, 'add_new.html', context)

