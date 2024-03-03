from django.shortcuts import render
from .models import addexpense

# Create your views here.
def expenseHome(request):
    context = {
        't':'expense Management',
        'expense':addexpense.objects.all()



    }
    return render(request,'expense.html',context)
    