from django.shortcuts import render, redirect
from .forms import OrderForm
from django.utils.timezone import now
from .models import models
from datetime import datetime
from orders.models import Order2, AutomobileOrder, WorkerOrder
from products.models import Product
from automobiles.models import Automobile
from workers.models import Worker


# Create your views here.

def order_view(request, pd_id):
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


def automobileorder_view(request, am_id):
    form = OrderForm()

    if request.method == 'POST':

        today = datetime.now()
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
            'total' : total,
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


def workerorder_view(request, wr_id):
    form = OrderForm()

    if request.method == 'POST':

        today = datetime.now()
        customer_name = request.user
        remarks = request.POST['remarks']

        workers = Worker.objects.get(pk=wr_id)
        worker_name = workers.name

        price = workers.rate

        total = float(workers.rate) * 1

        order = WorkerOrder()
        order.customer_name = customer_name
        order.worker_name = worker_name
        order.remarks = remarks
        order.order_date = today
        order.total_price = total

        order.save()

        context = {
            'today': today,
            'form': form,
            'total': total,
            'customer_name': customer_name,
            'worker_name': worker_name,
            'price': price,
            'date': today,
            'remarks': remarks,
            'id': wr_id,
        }

        return render(request, 'workerbill.html', context)


    else:
        today = datetime.now()

        current_user = request.user

        customer_name = (current_user.first_name + ' ' + current_user.last_name)

        workers = Worker.objects.get(pk=wr_id)
        worker_name = workers.name
        price = workers.rate

        context = {
            'today': today,
            'form': form,
            'customer_name': customer_name,
            'worker_name': worker_name,
            'price': price,
        }

        return render(request, 'workerorderform.html', context)


def trade_agreement_view(request):
    return render(request, 'Terms And Conditions.html')


