
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .models import Storage
from .form import *

def productList(request):
    if (request.method=='POST'):
        return redirect('user_Details')

    buyForm=BuyForm()
    products = Product.objects.order_by('-selling_price')
    return render(request,'product/productList.html',{'form':buyForm})


def addproduct(request):
    if (request.method=='POST'):
        addproductform = AddProductForm(request.POST)
        if addproductform.is_valid():
            addproductform.save()
        else:
            context = {
                'addproductform': addproductform,
            }
            return render(request, 'product/addproduct.html', context)
    else:
        addproductform = AddProductForm()
        context = {
            'addproductform': addproductform,
        }
        return render(request, 'product/addproduct.html', context)


def stockReport(request):
    stocks = Storage.objects.filter(stock=0).order_by('-stock_selling_price')
    return render(request,'product/stockReport.html',{'stocks':stocks})


