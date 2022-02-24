from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyAdminForm
from .models import MyAdmin
from remarks.models import Remark
from students.models import AppliedStudent, Student
from products.models import AppliedProduct, Product
from automobiles.models import AppliedAutomobile, Automobile
from workers.models import AppliedWorker, Worker
from insiders.models import Insider
from workers.forms import WorkerForm
from products.forms import ProductForm
from automobiles.forms import AutomobileForm
from students.forms import StudentForm
from orders.models import Order2, AutomobileOrder, WorkerOrder
from django.contrib import messages


# Create your views here.

def admins_view(request):
    if request.method == 'POST':
        found = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        alladmins = MyAdmin.objects.all()
        for admin in alladmins:
            if (admin.username == username) and (admin.password == password):
                found = True
            else:
                found = False
        if found:
            return redirect('adminhome/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('/myadmin/')
    else:
        return render(request, 'adminlogin.html')


def registeradmin_view(request):
    if request.method == 'POST':
        form = MyAdminForm(request.POST, request.FILES)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            admin = MyAdmin()
            admin.first_name = first_name
            admin.last_name = last_name
            admin.email = email
            admin.username = username
            admin.password = password2
            admin.save()
            return redirect('/myadmin/')

        else:
            messages.info(request, "Those Passwords do not match!")


    else:

        return render(request, 'registeradmin.html')


def adminhome_view(request):
    feedbacks = Remark.objects.all()
    epic = 0
    good = 0
    fine = 0
    bad = 0
    pathetic = 0
    for feedback in feedbacks:

        if feedback.remarks == 'Epic':
            epic += 1
        elif feedback.remarks == 'Good':
            good += 1
        elif feedback.remarks == 'Fine':
            fine += 1
        elif feedback.remarks == 'Bad':
            bad += 1
        else:
            pathetic += 1

        # For Gross Product Trade
        product_orders = Order2.objects.all()
        gross_product_trade = 0
        for order in product_orders:
            gross_product_trade += order.total_price

        # For Gross Automobile Trade
        gross_automobile_trade = 0
        automobile_orders = AutomobileOrder.objects.all()
        for order in automobile_orders:
            gross_automobile_trade += order.total_price

        # For Gross Worker Trade
        gross_worker_trade = 0
        worker_orders = WorkerOrder.objects.all()
        for order in worker_orders:
            gross_worker_trade += order.total_price

    context = {
        'feedbacks': feedbacks,
        'epic': epic,
        'good': good,
        'fine': fine,
        'bad': bad,
        'pathetic': pathetic,
        'gross_product_trade': gross_product_trade,
        'gross_automobile_trade': gross_automobile_trade,
        'gross_worker_trade': gross_worker_trade

    }
    return render(request, 'adminhome.html', context)


# Apps view
def adminapps_view(request):
    workers_no = 0
    products_no = 0
    automobiles_no = 0
    students_no = 0
    insiders_no = 0
    orders_no = 0

    workers = Worker.objects.all()
    products = Product.objects.all()
    automobiles = Automobile.objects.all()
    students = Student.objects.all()
    insiders = User.objects.all()
    orders1 = AutomobileOrder.objects.all()
    orders2 = Order2.objects.all()
    orders3 = WorkerOrder.objects.all()

    for worker in workers:
        workers_no += 1

    for product in products:
        products_no += 1

    for automobile in automobiles:
        automobiles_no += 1

    for student in students:
        students_no += 1

    for insider in insiders:
        insiders_no += 1

    for order1 in orders1:
        orders_no += 1
    for order2 in orders2:
        orders_no += 1
    for order3 in orders3:
        orders_no += 1

    context = {
        'workers_no': workers_no,
        'products_no': products_no,
        'automobiles_no': automobiles_no,
        'students_no': students_no,
        'insiders_no': insiders_no,
        'orders_no': orders_no,

    }

    return render(request, 'adminapps.html', context)


def adminadmins_view(request):
    admins = MyAdmin.objects.all()
    context = {
        'admins': admins,
    }

    return render(request, 'adminadmins.html', context)


def adminfeedbacks_view(request):
    feedbacks = Remark.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'adminfeedbacks.html', context)


def adminrequests_view(request):
    worker_requests = AppliedWorker.objects.all()
    automobile_requests = AppliedAutomobile.objects.all()
    product_requests = AppliedProduct.objects.all()
    student_requests = AppliedStudent.objects.all()

    wr = ar = pr = sr = 0

    for worker_request in worker_requests:
        wr += 1

    for automobile_request in automobile_requests:
        ar += 1

    for product_request in product_requests:
        pr += 1

    for student_request in student_requests:
        sr += 1

    context = {
        'wr': wr,
        'ar': ar,
        'pr': pr,
        'sr': sr,
    }

    return render(request, 'adminrequests.html', context)


def adminchart_view(request):
    return render(request, 'adminapps.html')


# Applied Requests views
def admin_applied_students_view(request):
    appliedstudents = AppliedStudent.objects.all()

    context = {
        'appliedstudents': appliedstudents,
    }
    return render(request, 'appliedstudents.html', context)


def admin_applied_products_view(request):
    appliedproducts = AppliedProduct.objects.all()

    context = {
        'appliedproducts': appliedproducts,
    }
    return render(request, 'appliedproducts.html', context)


def admin_applied_automobiles_view(request):
    appliedautomobiles = AppliedAutomobile.objects.all()

    context = {
        'appliedautomobiles': appliedautomobiles,
    }
    return render(request, 'appliedautomobiles.html', context)


def admin_applied_workers_view(request):
    appliedworkers = AppliedWorker.objects.all()

    context = {
        'appliedworkers': appliedworkers,
    }
    return render(request, 'appliedworkers.html', context)


# Admin app Views
def admin_workers_view(request):
    workers = Worker.objects.all()

    context = {
        'workers': workers,
    }
    return render(request, 'adminworkers.html', context)


def admin_products_view(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'adminproducts.html', context)


def admin_automobiles_view(request):
    automobiles = Automobile.objects.all()

    context = {
        'automobiles': automobiles,
    }
    return render(request, 'adminautomobiles.html', context)


def admin_students_view(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }
    return render(request, 'adminstudents.html', context)


def admin_insiders_view(request):
    insiders = User.objects.all()

    context = {
        'insiders': insiders,
    }
    return render(request, 'admininsiders.html', context)


def admin_orders_view(request):
    product_orders = Order2.objects.all()
    automobile_orders = AutomobileOrder.objects.all()
    worker_orders = WorkerOrder.objects.all()

    context = {
        'orders': product_orders,
        'automobile_orders': automobile_orders,
        'worker_orders': worker_orders,
    }
    return render(request, 'adminorders.html', context)


# Deleting views
def delete_worker(request, id):
    if request.method == 'POST':
        pi = Worker.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminworkers/')


def delete_automobile(request, id):
    if request.method == 'POST':
        pi = Automobile.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminautomobiles/')


def delete_product(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminproducts/')


def delete_student(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminstudents/')


def delete_insider(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/admininsiders/')


def delete_order(request, id):
    if request.method == 'POST':
        pi = Order2.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminorders/')


def delete_automobile_order(request, id):
    if request.method == 'POST':
        pi = AutomobileOrder.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminorders/')


def delete_worker_order(request, id):
    if request.method == 'POST':
        pi = WorkerOrder.objects.get(pk=id)
        pi.delete()
        return redirect('/myadmin/adminorders/')


# Decline views
def decline_automobile_view(request, id):
    if request.method == 'POST':
        obj = AppliedAutomobile.objects.get(pk=id)
        obj.delete()
        return redirect('/myadmin/admin_applied_automobiles/')


def decline_worker_view(request, id):
    if request.method == 'POST':
        obj = AppliedWorker.objects.get(pk=id)
        obj.delete()
        return redirect('/myadmin/admin_applied_workers/')


def decline_product_view(request, id):
    if request.method == 'POST':
        obj = AppliedProduct.objects.get(pk=id)
        obj.delete()
        return redirect('/myadmin/admin_applied_products/')


def decline_student_view(request, id):
    if request.method == 'POST':
        obj = AppliedStudent.objects.get(pk=id)
        obj.delete()
        return redirect('/myadmin/admin_applied_students/')


# Approve Views
def approve_worker_view(request, id):
    if request.method == 'POST':
        obj = AppliedWorker.objects.get(pk=id)
        form = WorkerForm(request.POST, request.FILES)

        id = id
        name = obj.name
        email = obj.email
        rate = obj.rate
        status = obj.status

        worker = Worker()
        worker.name = name
        worker.email = email
        worker.rate = rate
        worker.status = status

        worker.save()
        obj.delete()

        return redirect('/myadmin/admin_applied_workers/')


def approve_product_view(request, id):
    if request.method == 'POST':
        obj = AppliedProduct.objects.get(pk=id)

        prd = Product()
        prd.name = obj.name
        prd.image = obj.image
        prd.price = obj.price
        prd.description = obj.description
        prd.status = obj.status
        prd.save()
        obj.delete()

        return redirect('/myadmin/admin_applied_products/')


def approve_automobile_view(request, id):
    if request.method == 'POST':
        obj = AppliedAutomobile.objects.get(pk=id)

        atm = Automobile()

        atm.name = obj.name
        atm.image = obj.image
        atm.price = obj.price
        atm.description = obj.description
        atm.status = obj.status
        atm.save()
        obj.delete()

        return redirect('/myadmin/admin_applied_automobiles/')


def approve_student_view(request, id):
    if request.method == 'POST':
        obj = AppliedStudent.objects.get(pk=id)

        std = Student()

        std.name = obj.name
        std.email = obj.email
        std.address = obj.address
        std.state = obj.state
        std.course = obj.course
        std.message = obj.message

        std.save()
        obj.delete()

        return redirect('/myadmin/admin_applied_students/')


# Update views

def update_worker_view(request, pk):

    worker = Worker.objects.get(id=pk)
    form = WorkerForm(instance=worker)

    if request.method == 'POST':
        form1 = WorkerForm(request.POST, instance=worker)
        if form1.is_valid():
            form1.save()
            return redirect('/myadmin/adminworkers/')

    context = {
        'form': form,
    }
    return render(request, 'updateworkerform.html', context)


def update_product_view(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        form1 = ProductForm(request.POST, instance=product)
        if form1.is_valid():
            form1.save()
            return redirect('/myadmin/adminproducts/')

    context = {
        'form': form,
    }
    return render(request, 'updateproductform.html', context)


def update_automobile_view(request, id):
    automobile = Automobile.objects.get(id=id)
    form = AutomobileForm(instance=automobile)
    if request.method == 'POST':
        automobile = Automobile.objects.get(pk=id)
        form1 = AutomobileForm(request.POST, instance=automobile)
        if form1.is_valid():
            form1.save()
            return redirect('/myadmin/adminautomobiles/')

    context = {
        'form': form,
    }
    return render(request, 'updateautomobileform.html', context)


def update_student_view(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form1 = StudentForm(request.POST, instance=student)
        if form1.is_valid():
            form1.save()
            return redirect('/myadmin/adminstudents/')

    context = {
        'form': form,
    }
    return render(request, 'updatestudentform.html', context)


# add items to apps views
def add_worker_view(request):
    form = WorkerForm()

    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/myadmin/adminworkers/')

    context = {'form': form}

    return render(request, 'joinform.html', context)


def add_product_view(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/myadmin/adminproducts/')

    context = {
        'form': form
    }

    return render(request, 'addproduct.html', context)


def add_automobile_view(request):
    form = AutomobileForm()

    if request.method == 'POST':
        form = AutomobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/myadmin/adminautomobiles/')

    context = {
        'form': form
    }

    return render(request, 'postautomobile.html', context)


def add_student_view(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/myadmin/adminstudents/')

    context = {
        'form': form
    }

    return render(request, 'studentform.html', context)


def add_insider_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()
        return redirect('/insiders/')





    else:
        context = {}

        return render(request, 'adminaddinsider.html', context)


# delete feedback

def delete_feedback(request, fb_id):
    if request.method == 'POST':
        feedback = Remark.objects.get(pk=fb_id)
        feedback.delete()
        return redirect('/myadmin/adminhome/adminfeedbacks/')
