from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

def home(request):
    orders = Order.objects.all()
    return render(request, 'app3/home.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app3-home')
    else:
        form = OrderForm()
    return render(request, 'app3/add_order.html', {'form': form})
