from django.contrib import admin
from django.urls import path, include

from .views import admins_view, registeradmin_view, \
    adminhome_view, admin_applied_students_view, \
    admin_applied_products_view, admin_applied_automobiles_view, \
    admin_applied_workers_view, admin_workers_view, admin_products_view, \
    admin_students_view, admin_insiders_view, admin_orders_view, \
    admin_automobiles_view, delete_worker, \
    delete_automobile, delete_product, \
    delete_student, delete_insider, delete_order, \
    delete_automobile_order, delete_worker_order, \
    decline_automobile_view, decline_worker_view, \
    decline_product_view, decline_student_view, \
    update_worker_view, update_product_view, \
    update_automobile_view, update_student_view, \
    adminapps_view, adminadmins_view, \
    adminfeedbacks_view, adminrequests_view, \
    adminchart_view, \
    approve_worker_view, approve_automobile_view, \
    approve_product_view, approve_student_view, \
    add_worker_view, add_product_view, add_student_view, \
    add_automobile_view, add_insider_view, \
    delete_feedback

urlpatterns = [
    # base admin urls
    path('', admins_view),
    path('registeradmin/', registeradmin_view),
    path('adminhome/', adminhome_view),

    # View applied requests
    path('admin_applied_workers/', admin_applied_workers_view),
    path('admin_applied_automobiles/', admin_applied_automobiles_view),
    path('admin_applied_products/', admin_applied_products_view),
    path('admin_applied_students/', admin_applied_students_view),

    # view apps in admin panel
    path('adminworkers/', admin_workers_view),
    path('adminautomobiles/', admin_automobiles_view),
    path('adminproducts/', admin_products_view),
    path('adminstudents/', admin_students_view),
    path('admininsiders/', admin_insiders_view),
    path('adminorders/', admin_orders_view),

    # delete urls
    path('deleteworker/<int:id>/', delete_worker, name='deleteworker'),
    path('deleteautomobile/<int:id>/', delete_automobile, name='deleteautomobile'),
    path('deleteproduct/<int:id>/', delete_product, name='deleteproduct'),
    path('deletestudent/<int:id>/', delete_student, name='deletestudent'),
    path('deleteinsider/<int:id>/', delete_insider, name='deleteinsider'),
    path('deleteorder/<int:id>/', delete_order, name='deleteorder'),
    path('deleteautomobileorder/<int:id>/', delete_automobile_order, name='deleteautomobileorder'),
    path('deleteworkerorder/<int:id>/', delete_worker_order, name='deleteworkerorder'),

    # add items to apps urls
    path('addworker/', add_worker_view, name='addworker'),
    path('addproduct/', add_product_view, name='addproduct'),
    path('addautomobile/', add_automobile_view, name='addautomobile'),
    path('addstudent/', add_student_view, name='addstudent'),
    path('addinsider/', add_insider_view, name='addinsider'),

    # decline urls
    path('declineworker/<int:id>/', decline_worker_view, name='declineworker'),
    path('declineproduct/<int:id>/', decline_product_view, name='declineproduct'),
    path('declineautomobile/<int:id>/', decline_automobile_view, name='declineautomobile'),
    path('declinestudent/<int:id>/', decline_student_view, name='declinestudent'),

    # approve urls
    path('approveworker/<int:id>/', approve_worker_view, name='approveworker'),
    path('approveproduct/<int:id>/', approve_product_view, name='approveproduct'),
    path('approveautomobile/<int:id>/', approve_automobile_view, name='approveautomobile'),
    path('approvestudent/<int:id>/', approve_student_view, name='approvestudent'),

    # update urls
    path('updateworker/<int:pk>/', update_worker_view, name='updateworker'),
    path('updateproduct/<int:id>/', update_product_view, name='updateproduct'),
    path('updateautomobile/<int:id>/', update_automobile_view, name='updateautomobile'),
    path('updatestudent/<int:id>/', update_student_view, name='updatestudent'),

    # show apps urls
    path('adminhome/adminapps/', adminapps_view),
    path('adminhome/adminadmins/', adminadmins_view),
    path('adminhome/adminfeedbacks/', adminfeedbacks_view),
    path('adminhome/adminrequests/', adminrequests_view),
    path('adminhome/adminchart/', adminchart_view),

    #delete remarks urls
    path('deletefeedback/<int:fb_id>', delete_feedback, name='deletefeedback'),

]
