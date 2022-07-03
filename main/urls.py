from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView
import  main.ajaxcalls as ajxcl

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
    path('registered/', views.registred_response, name='registred_response'),


]

urlpatterns += (
    path('wardrobes-storage-units/', TemplateView.as_view(template_name='main/wardrobes-&-storage-units.html'), name='wardrobes-storage-units'),
    path('entertainment-unit/', TemplateView.as_view(template_name='main/entertainment-unit.html'), name='entertainment-unit'),
    path('study-units/', TemplateView.as_view(template_name='main/study-units.html'), name='study-units'),
    path('puja-units/', TemplateView.as_view(template_name='main/puja-units.html'), name='puja-units'),
    path('bedroom/', TemplateView.as_view(template_name='main/bedroom.html'), name='bedroom'),
    path('movable-furnitures/', TemplateView.as_view(template_name='main/movable-furnitures.html'), name='movable-furnitures'),
    path('modular-kitchen/', TemplateView.as_view(template_name='main/modular-kitchen.html'), name='modular-kitchen'),
    path('children-room/', TemplateView.as_view(template_name='main/children-room.html'), name='children-room'),
    path('false-ceiling/', TemplateView.as_view(template_name='main/false-ceiling.html'), name='false-ceiling'),
    path('crockery-units/', TemplateView.as_view(template_name='main/crockery-units.html'), name='crockery-units'),
    path('living-room/', TemplateView.as_view(template_name='main/living-room.html'), name='living-room'),
    path('cookery-shoe-rack/', TemplateView.as_view(template_name='main/cookery-&-shoe-rack.html'), name='cookery-shoe-rack'),
    path('contact-us/', TemplateView.as_view(template_name='main/contact-us.html'), name='contact-us'),
    path('our-projects/', TemplateView.as_view(template_name='main/our-projects.html'), name='our-projects'),
)

urlpatterns += (
    path('ajax_call/expert-call-back/', ajxcl.expert_call, name='expert-call'),
    path('ajax_call/contact-us-call/', ajxcl.contact_us_call, name='contact-us-call'),



    
)
