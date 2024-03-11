from django.shortcuts import render
from .models import sales
from .forms import salesForm



# Create your views here.
def saleshome(request):
    form = salesForm()

    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = sales.objects.get(id=pk)
                items = salesForm(request.POST,instance=item)
            else: 
                items = salesForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = sales.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = sales.objects.get(id=pk)
            form = salesForm(instance=item)   
    context = {
        'forms': form, 
        't':'Sales Management',
        'sales':sales.objects.all()
    }
    return render(request,'sales.html',context)