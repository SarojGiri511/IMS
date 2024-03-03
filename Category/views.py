from django.shortcuts import render
from .models import Category


# Create your views here.
def CategoryHome(request):
     context = {
        't':'Category Management',
        'Category':Category.objects.all()



    }
     return render(request,'categories.html',context)
