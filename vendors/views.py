from django.shortcuts import render
from .models import vendors


# Create your views here.
def vendorHome(request):
    context = {
        't':'Vendor Management',
        'vendor':vendors.objects.all()



    }
    return render(request, 'vendor.html',context)