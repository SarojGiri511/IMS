from django.shortcuts import render
from .models import Product
from .forms import ProductForm



# Create your views here.
def ProductHome(request):
    form = ProductForm()
    if request.method == 'POST':
        if 'save' in request.POST:
            Product_add_edit(request)            
        elif 'delete' in request.POST:
            Product_delete(request)
        elif 'edit' in request.POST:
            form = Product_edit(request)

    context = {
        'forms': form,
        'title':'Products',
        'Products':Product.objects.all().order_by('-id') #TO get all data from product table latest first
       
    }
    
    return render(request,'index.html', context)


def Product_add_edit(request):
    if request.POST.get('save'):
        pk = request.POST.get('save')
        item = Product.objects.get(id=pk)
        items = ProductForm(request.POST, request.FILES, instance=item)
    else: 
        items = ProductForm(request.POST, request.FILES)
    if items.is_valid:
        items.save()
        
    else:
       return 'Error During Validation'


def Product_delete(request):
    pk = request.POST.get('delete')
    item = Product.objects.filter(id=pk)
    item.delete()


def Product_edit(request):
    pk = request.POST.get('edit')
    item = Product.objects.get(id=pk)
    return ProductForm(instance=item)   



def ProductDetail(request):
    return render(request, 'detail.html')

def ProductAdd(request):
 
    context = {
        'submit_url':'product',
        'forms':  ProductForm(), 
    }
    return render(request, 'add_new.html', context)