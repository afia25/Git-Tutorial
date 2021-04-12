from django.shortcuts import render
from .models import Order_item
from customer.models import Payment

def allInvoices(request):
    invoices=Order_item.objects.all()
    return render(request,'order_item/allInvoices.html',{'invoices':invoices})

def prod1Invoice(request):
    return render(request,'order_item/prod1Invoice.html')

def prod2Invoice(request):
    return render(request,'order_item/prod2Invoice.html')

def prod3Invoice(request):
    return render(request,'order_item/prod3Invoice.html')




def allDueReport(request):
    return render(request,'order_item/allDueReport.html')

def customerWiseDueReport(request):
    ps=Payment.objects.all()
    return render(request,'order_item/customerWiseDueReport.html',{'ps':ps})

def productWiseDueReport(request):
    return render(request,'order_item/productWiseDueReport.html')




def salesReport(request):
    return render(request,'order_item/salesReport.html')

def customerWiseSalesReport(request):
    return render(request,'order_item/customerWiseSalesReport.html')

def productWiseSalesReport(request):
    return render(request,'order_item/productWiseSalesReport.html')