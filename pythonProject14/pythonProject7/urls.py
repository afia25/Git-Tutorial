"""pythonProject7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from customer import views as views1
from product import views as viewsprod
from order_item import views as viewsorder
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),


    path('register/',views1.register,name='register'),
    path('base/',views1.base),
    path('',views1.home,name='home'),
    path('user_Details/',views1.user_Details,name='user_Details'),
    path('profile/',views1.profile,name='profile'),
    path('profileUpdate/',views1.profileUpdate,name='profileUpdate'),

    path('login/',auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('accounts/profile/',views1.profile),
    path('logout/',auth_views.LogoutView.as_view(template_name='customer/logout.html'), name='logout'),


    path('productList/',viewsprod.productList,name='productList'),
    path('stock/',viewsprod.stockReport,name='stock'),
    path('addproduct/',viewsprod.addproduct,name='addproduct'),


    path('customerInfo/',views1.customerInfo,name='customerInfo'),
    path('allInvoices/',viewsorder.allInvoices,name='allInvoices'),
    path('prod1Invoice/', viewsorder.prod1Invoice),
    path('prod2Invoice/', viewsorder.prod2Invoice),
    path('prod3Invoice/', viewsorder.prod3Invoice),
    path('allDueReport/', viewsorder.allDueReport),
    path('customerWiseDueReport/', viewsorder.customerWiseDueReport),
    path('productWiseDueReport/', viewsorder.productWiseDueReport),
    path('salesReport/', viewsorder.salesReport),
    path('customerWiseSalesReport/', viewsorder.customerWiseSalesReport),
    path('productWiseSalesReport/', viewsorder.productWiseSalesReport)




]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
