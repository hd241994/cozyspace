from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_1', views.form_1, name='form_1'),
    path('form_2', views.form_2, name='form_2'),
    path('form_3', views.form_3, name='form_3'),
    path('otp-validation', views.otp_validation, name='otp-validation'),
    path('reno', views.renovation, name='reno'),
    path('send-otp', views.send_otp, name='send-otp'),
    path('customer-list/', views.customers_list, name='customer-list'),
    path('customer/<int:pk>', views.customer_detail, name='customer'),
    path('delete/<int:pk>', views.delete_customer, name='customer_delete'),

]