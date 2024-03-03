from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def productHome(request):
    form = ProductForm()
    
    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Product.objects.get(id=pk)
                items = ProductForm(request.POST,instance=item)
            else: 
                items = ProductForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Product.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Product.objects.get(id=pk)
            form = ProductForm(instance=item)   

    context = {
        'forms': form,
        'title':'Products',
        'products':Product.objects.all().order_by('-id') #TO get all data from product table latest first
    }
    
    return render(request,'index.html', context)

def ProductDetail(request):
    return render(request, 'detail.html')
