from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse



# Create your views here.
def ExpenseHome(request):
    form = ExpenseForm()
   
    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Expense.objects.get(id=pk)
                items = ExpenseForm(request.POST,instance=item)
            else: 
                items = ExpenseForm(request.POST)
            items.save()
            
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Expense.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Expense.objects.get(id=pk)
            form = ExpenseForm(instance=item)   

    
    context = {
        'forms': form, 
        't':'Expense Management',
        'expenses':Expense.objects.all()
    }
    return render(request,'expense.html',context)

def ExpenseAdd(request):
 
    context = {
        'submit_url':'expense',
        'forms':  ExpenseForm(), 
    }
    return render(request, 'add_new.html', context)




    