from django.shortcuts import render
from .models import expense
from .forms import expenseForm
from django.http import HttpResponse



# Create your views here.
def expenseHome(request):
    form = expenseForm()
   
    if request.method == 'POST':
        items = expenseForm(request.POST.form)
        items.save()
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = expense.objects.get(id=pk)
                items = expenseForm(request.POST,instance=item)
            else: 
                items = expenseForm(request.POST)
            items.save()
            
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = expense.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = expense.objects.get(id=pk)
            form = expenseForm(instance=item)   

    
    context = {
        'forms': form, 
        't':'expense Management',
        'expense':expense.objects.all()
    }
    return render(request,'expense.html',context)


    