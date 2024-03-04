from django.shortcuts import render
from .models import Category
from .forms import CategoryForm


# Create your views here.
def CategoryHome(request):
    form = CategoryForm()


    if request.method == 'POST':
        if 'save' in request.POST:
           
            if request.POST.get('save'):
                pk = request.POST.get('save')
                item = Category.objects.get(id=pk)
                items = CategoryForm(request.POST,instance=item)
            else: 
                items = CategoryForm(request.POST)
            items.save()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            item = Category.objects.filter(id=pk)
            item.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            item = Category.objects.get(id=pk)
            form = CategoryForm(instance=item)   

    
    
  
    context = {
        'forms': form, 
        't':'Category Management',
        'Category':Category.objects.all()



    }
    return render(request,'categories.html',context)