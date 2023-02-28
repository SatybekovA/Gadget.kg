from django.shortcuts import render, redirect
from .models import Location, Product
from .forms import LocationForm, ProductForm



def location(request):
    location = Location.objects.all()
    context = {'location': location}
    return render(request, 'location.html', context)


def product(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'product.html', context)


def location_create(request):
    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('markets:location')
    context = {'form': form}
    return render(request, 'location_create.html', context)


def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('markets:product')
    context = {'form': form}
    return render(request, 'product_create.html', context)


def location_update(request, pk):
    location = Location.objects.get(id=pk)
    form = LocationForm(instance=location)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('markets:location')
    context = {'form': form}
    return render(request, 'location_create.html', context)


def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('markets:product')
    context = {'form': form}
    return render(request, 'product_create.html', context)


def location_delete(request, pk):
    location = Location.objects.get(id=pk)
    location.delete()
    return redirect('markets:location')


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('markets:product')