from django.shortcuts import render
from django.http import HttpResponse
from .models import sales


# Create your views here.
def saleshome(request):
    context = {
        't':'Sales Management',
        'sales':sales.objects.all()
    }
    return render(request,'sales.html',context)