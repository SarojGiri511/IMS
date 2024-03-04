from django.shortcuts import render
from .models import addexpense
from .forms import expenseForm


# Create your views here.
def expenseHome(request):
    form = expenseForm()
    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = addexpense.objects.get(id=pk)
                items = expenseForm(request.POST,instance=item)
            else: 
                items = expenseForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = addexpense.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = addexpense.objects.get(id=pk)
            form = expenseForm(instance=item)   

    
    context = {
        'forms': form, 
        't':'expense Management',
        'expense':addexpense.objects.all()
    }
    return render(request,'expense.html',context)


    