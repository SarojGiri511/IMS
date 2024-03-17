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


from Product.views import ProductHome, ProductDetail
from Product.views import ProductAdd

from Purchase.views import PurchaseHome, PurchaseAdd
from Inventory.views import InventoryHome, InventoryAdd
from Vendors.views import VendorHome, VendorAdd
from Expense.views import ExpenseHome, ExpenseAdd
from Category.views import  CategoryHome, CategoryAdd
from Order.views import OrderHome, OrderAdd
from Sales.views import Saleshome, SalesAdd
from Customer.views import Customerhome, CustomerAdd
from django.conf import settings
from django.conf.urls.static import static #Static Files
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('IMS/', sign, name='sign'),
    path('products/', ProductHome, name='product'),
    path('product/add/', ProductAdd, name='product.add'),
    path('inventory/', InventoryHome, name='inventory'),
    path('inventory/add/', InventoryAdd, name='inventory.add'),
    path('vendors/', VendorHome, name='vendor'),

    path('vendors/add/', VendorAdd, name='vendor.add'),

    path('expense/', ExpenseHome, name='expense'),
    path('expense/add/', ExpenseAdd, name='expense.add'),

    path('category/', CategoryHome, name='category'),
    path('category/add/', CategoryAdd, name='category.add'),

    path('order/',OrderHome,name='order'),
    path('order/add/',OrderAdd,name='order.add'),

    path('sales/',Saleshome,name='sales'),
    path('sales/add/',SalesAdd,name='sales.add'),

    path('customer/',Customerhome,name='customer'),
    path('customer/add/',CustomerAdd,name='customer.add'),

    path('products/detail/', ProductDetail, name='roductDetail'),
    path('purchases/', PurchaseHome, name='purchase'),
    path('purchases/add/', PurchaseAdd, name='purchase.add'),

    path('admin/', admin.site.urls),
    path('admin/logout/', auth_views.LogoutView.as_view(), name='admin_logout'),
    path('admin/login/', auth_views.LoginView.as_view(), name='admin_login'),



    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Static FILES
