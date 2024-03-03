from django.shortcuts import render
from .models import customer


# Create your views here.
def customerhome(request):
    context = {
        't':'Customer Management',
        'customer':customer.objects.all()



    }
    return render(request,'customer.html',context)