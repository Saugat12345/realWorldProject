from django.shortcuts import render, redirect
from .forms import ProductForm, AppliedProductForm
from .models import Product, AppliedProduct
from django.contrib.auth.decorators import login_required

# Create your views here.
def product_view(request):
    product = Product()
    products =Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products.html', context)

# @login_required
def addproduct_view(request):
    form = AppliedProductForm()

    if request.method == 'POST':
        form = AppliedProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/')

    context = {
        'form': form
    }

    return render(request, 'addproduct.html', context)





