from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

def home(request):
    customers = Customer.objects.all()
    return render(request, 'app2/home.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app2-home')
    else:
        form = CustomerForm()
    return render(request, 'app2/add_customer.html', {'form': form})
