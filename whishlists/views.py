from django.shortcuts import render, redirect, HttpResponseRedirect
from products.models import Product
from datetime import datetime
from .models import ProductWishlist, AutomobileWishlist
from automobiles.models import Automobile
from orders.views import Order2, OrderForm, AutomobileOrder


# Create your views here.

def save_productwishlist(request, pd_id):
    if request.method == 'POST':
        current_user = request.user

        product = Product.objects.get(pk=pd_id)
        status = product.status
        product_id = product.id
        product_status = product.status

        customer_id = current_user.id
        customer_name = (current_user.first_name) + ' ' + (current_user.last_name)
        date = datetime.now()
        wish_name = product.name
        price = product.price

        productwhishlist = ProductWishlist()
        productwhishlist.date = date
        productwhishlist.customer_id = customer_id
        productwhishlist.customer_name = customer_name
        productwhishlist.product_name = wish_name
        productwhishlist.price = price
        productwhishlist.product_status = product_status
        productwhishlist.product_id = pd_id

        productwhishlist.save()

        return redirect('/products/')


def save_automobilewishlist(request, am_id):
    if request.method == 'POST':
        current_user = request.user
        automobile = Automobile.objects.get(pk=am_id)
        automobile_status = automobile.status

        customer_id = current_user.id
        customer_name = (current_user.first_name) + ' ' + (current_user.last_name)
        date = datetime.now()
        wish_name = automobile.name
        price = automobile.price

        automobilewhishlist = AutomobileWishlist()
        automobilewhishlist.date = date
        automobilewhishlist.customer_id = customer_id
        automobilewhishlist.customer_name = customer_name
        automobilewhishlist.automobile_name = wish_name
        automobilewhishlist.price = price
        automobilewhishlist.automobile_status = automobile_status
        automobilewhishlist.automobile_id = am_id
        automobilewhishlist.save()

        return redirect('/automobiles/')


def wishlist_view(request):
    current_user = request.user
    current_userId = current_user.id

    productwishlist = ProductWishlist.objects.all()
    automobilewishlist = AutomobileWishlist.objects.all()

    auto_name = Automobile.objects

    context = {
        'productwishlist': productwishlist,
        'automobilewishlist': automobilewishlist,
        'current_userId': current_userId,
        'auto_name': auto_name,
    }
    return render(request, 'basewishlist.html', context)


## Delete wishes
def delete_productwish(request, wish_id):
    if request.method == 'POST':
        obj = ProductWishlist.objects.get(pk=wish_id)
        obj.delete()
        return redirect('/whishlists/')


def delete_automobilewish(request, wish_id):
    if request.method == 'POST':
        obj = AutomobileWishlist.objects.get(pk=wish_id)
        obj.delete()
        return redirect('/whishlists/')


# Order Wishes
def order_productwish(request, pd_id):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        today = datetime.now()
        customer_name = request.user.first_name + ' ' + request.user.last_name
        quantity = request.POST['quantity']
        remarks = request.POST['remarks']

        products = Product.objects.get(pk=pd_id)
        product_name = products.name

        total = float(products.price) * float(quantity)

        order = Order2()
        order.customer_name = customer_name
        order.product_name = product_name
        order.quantity = quantity
        order.remarks = remarks
        order.order_date = today
        order.total_price = total

        order.save()
        context = {
            'total': total,
            'customer_name': customer_name,
            'product_name': product_name,
            'quantity': quantity,
            'date': today,
            'remarks': remarks,
            'id': pd_id,

        }

        return render(request, 'bill.html', context)


    else:
        today = datetime.now()

        current_user = request.user
        customer_name = (current_user.first_name + ' ' + current_user.last_name)

        products = Product.objects.get(pk=pd_id)
        product_name = products.name
        price = products.price

        context = {
            'today': today,
            'form': form,
            'customer_name': customer_name,
            'product_name': product_name,
            'price': price,
        }

        return render(request, 'orderform.html', context)


def order_automobilewish(request, am_id):
    form = OrderForm()

    if request.method == 'POST':
        today = datetime.now()

        current_user = request.user

        customer_name = (current_user.first_name + ' ' + current_user.last_name)
        quantity = request.POST['quantity']

        remarks = request.POST['remarks']

        automobiles = Automobile.objects.get(pk=am_id)
        autombile_name = automobiles.name

        total = float(automobiles.price) * float(quantity)

        order = AutomobileOrder()
        order.customer_name = customer_name
        order.automobile_name = autombile_name
        order.quantity = quantity
        order.remarks = remarks
        order.order_date = today
        order.total_price = total

        order.save()

        automobiles = Automobile.objects.get(pk=am_id)
        automobile_name = automobiles.name
        price = automobiles.price

        context = {
            'today': today,
            'form': form,
            'total': total,
            'customer_name': customer_name,
            'automobile_name': automobile_name,
            'price': price,
            'quantity': quantity,
            'date': today,
            'remarks': remarks,
            'id': am_id,
        }

        return render(request, 'automobilebill.html', context)


    else:
        today = datetime.now()

        current_user = request.user

        customer_name = (current_user.first_name + ' ' + current_user.last_name)

        automobiles = Automobile.objects.get(pk=am_id)
        automobile_name = automobiles.name
        price = automobiles.price

        context = {
            'today': today,
            'form': form,
            'customer_name': customer_name,
            'automobile_name': automobile_name,
            'price': price,
        }

        return render(request, 'automobileorderform.html', context)
