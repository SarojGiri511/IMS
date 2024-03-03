"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home
from .views import sign


from product.views import productHome, ProductDetail
from purchase.views import PurchaseDetail
from Inventory.views import InventoryHome
from vendors.views import vendorHome
from addexpense.views import expenseHome
from Category.views import  CategoryHome
from order.views import orderHome
from sales.views import saleshome
from customer.views import customerhome
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('IMS/', sign, name='sign'),
    path('products/', productHome, name='product'),
    path('inventory/', InventoryHome, name='inventory'),
    path('vendors/', vendorHome, name='vendor'),
    path('expense/', expenseHome, name='expense'),
    path('category/', CategoryHome, name='category'),
    path('order/',orderHome,name='order'),
    path('sales/',saleshome,name='sales'),
    path('customer/',customerhome,name='customer'),
    path('products/detail/', ProductDetail, name='productDetail'),
    path('purchases/', PurchaseDetail, name='purchase'),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
