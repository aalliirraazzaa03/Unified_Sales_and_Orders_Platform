from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect

def home(request):
    products = Product.objects.all()
    return render(request, 'app1/home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1-home')
    else:
        form = ProductForm()
    return render(request, 'app1/add_product.html', {'form': form})
