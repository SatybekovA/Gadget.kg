from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Employee, Order
from .forms import CustomerForm, EmployeeForm, OrderForm
from django.db.models import Sum


def main(request):
    main = Customer.objects.all()
    return render(request,'main.html', {'main':main})


def customer(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer.html', context)

def employee(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee.html', context)

def order(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order.html', context)


def customer_create(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:customers')
    context = {'form': form}
    return render(request, 'customer_create.html', context)
    

def employee_create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employees')
    context = {'form': form}
    return render(request, 'employee_create.html', context)
    
def order_create(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:orders')
    context = {'form': form}
    return render(request, 'order_create.html', context)


def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('dashboard:customers')


def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('dashboard:employees')



def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('dashboard:orders')


def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('dashboard:customers')
    context = {'form': form}
    return render(request, 'customer_create.html', context)


def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employees')
    context = {'form': form}
    return render(request, 'employee_create.html', context)


def order_update(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard:orders')
    context = {'form': form}
    return render(request, 'order_create.html', context)



