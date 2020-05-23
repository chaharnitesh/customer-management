from django.shortcuts import render,redirect
from .models import Order,Customer,Product
from .forms import OrderForm
from django.forms import inlineformset_factory

# Create your views here.


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    
    context = {'customers': customers,'orders': orders,
	'total_orders': total_orders, 'pending': pending,'delivered': delivered, }
    return render(request,'crmapp/dashboard.html',context)

def product(request):
    products = Product.objects.all()

    return render(request,'crmapp/product.html',{'product':products})

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    print(customer)
    orders = customer.order_set.all()
    print(orders)
	
    order_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request,'crmapp/customer.html',context)

def createorder(request,pk):
    customer =Customer.objects.get(id=id)
    form = OrderForm()
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request,'crmapp/order_form.html',context)

def updateorder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():  
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request,'crmapp/order_form.html',context)

def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method =='POST':
         order.delete()
         return redirect('/')
    
    context = {'order':order}
    return render(request,'crmapp/order_delete.html',context)

