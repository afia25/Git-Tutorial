

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Products
from django.contrib import messages
from .models import *

from .form import *




def productList(request):
    if (request.method=='POST'):
        return redirect('userorder')

    buyForm=BuyForm()
    return render(request,'product/productList.html',{'form':buyForm})





def clothes(request):
    if (request.method=='POST'):
        clothesform=ClothesForm(request.POST)
        if (clothesform.is_valid()):
            clothesform.save()
            return redirect('productList')
        else:
            return render(request, 'product/clothes.html', {'clothesform': clothesform})
    else:
        clothesform = ClothesForm()
        return render(request, 'product/clothes.html', {'clothesform': clothesform})


def electronics(request):
    if (request.method=='POST'):
        electronicsform=ElectronicsForm(request.POST)
        if (electronicsform.is_valid()):
            electronicsform.save()
            return redirect('productList')
        else:
            return render(request, 'product/electronics.html', {'electronicsform': electronicsform})
    else:
        electronicsform = ElectronicsForm()
        return render(request, 'product/electronics.html', {'electronicsform': electronicsform})






    #buyForm=BuyForm()
    #return render(request,'product/clothes.html',{'form':buyForm})

def food(request):
    if (request.method=='POST'):
        foodform=FoodForm(request.POST)
        if (foodform.is_valid()):
            foodform.save()
            return redirect('productList')
        else:
            return render(request, 'product/food.html', {'foodform': foodform})
    else:
        foodform = FoodForm()
        return render(request, 'product/food.html', {'foodform': foodform})



def order(request):
    orders = Order.objects.all()
    return render(request,'product/order.html',{'orders':orders})


def userorder(request):
    if (request.method=='POST'):
        return redirect('productList')

    userorderform = UserOrderForm()
    orders = Order.objects.all()
    return render(request, 'product/userorder.html', {'orders': orders, 'userorderform': userorderform})


    #return render(request,'product/productList.html',{'form':buyForm})







def stockReport(request):
    stocks = Products.objects.all()
    return render(request,'product/stockReport.html',{'stocks':stocks})


def makeinvoice(request):
    invoices=Invoice.objects.all()
    return render(request, 'product/makeinvoice.html', {'invoices':invoices})
    #if (request.method == "POST"):

def due(request):
    invoices=Invoice.objects.all()
    return render(request, 'product/due.html', {'invoices':invoices})

def outOfStock(request):
    products=Products.objects.filter(stock=0)
    return render(request, 'product/outOfStock.html', {'products':products})



def addproduct(request):
    if (request.method=="POST"):
        addproductform = AddProductForm(request.POST)
        if (addproductform.is_valid()):
            addproductform.save()

           # views1.stock(request)
            return redirect('adminHome')
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


def invoice(request):
    if (request.method=="POST"):
        invoiceform = InvoiceForm(request.POST)
        if (invoiceform.is_valid()):
            invoiceform.save()
            return redirect('home')
        else:
            context = {
                'invoiceform': invoiceform,
            }
            return render(request, 'product/invoice.html', context)
    else:
        invoiceform = InvoiceForm()
        context = {
            'invoiceform': invoiceform,
        }
        return render(request, 'product/invoice.html', context)


def salesReport(request):
    pass



