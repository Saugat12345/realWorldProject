from django.contrib import admin
from django.urls import path, include
from .views import insiderlogin_view, insiderregister_view, loguout_view, \
    insider_deleteaccount_view, MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'users'

urlpatterns = [
    path('', insiderlogin_view),
    path('insiderregister/', insiderregister_view),
    path('logout/', loguout_view),

    path('editprofile/', MyPasswordChangeView.as_view(), name='editprofile'),
    path('editprofiledone/', MyPasswordResetDoneView.as_view(), name='editprofiledone'),

    path('deleteaccount/', insider_deleteaccount_view),
]
