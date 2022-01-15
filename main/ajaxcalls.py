from cozyspace import settings
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import (api_view, authentication_classes,
                                       parser_classes, permission_classes)
                                       
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from .emailAPI import EmailSending


@api_view(["POST"])
@csrf_exempt
def expert_call(request):
    try:
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # url = f'https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/ADDON_SERVICES/SEND/TSMS'
                 
        # payload = {
        #     "From": "cozysp",
        #     "To": "7008975760,", 
        #     "TemplateName": "Admin MSG", 
        #     "VAR1":name, 
        #     "VAR2": phone,
        #     # "VAR3":name, 
        #     # "VAR4": phone,
        #     # "VAR5":name, 
        #     # "VAR6": phone
        #     }
        emailobj = EmailSending()
        emailobj.sub = "EXPERT CALL BACK"
        # emailobj.to = 'avsr94@gmail.com'
        emailobj.body = f'''
        Name of Customer: {name},
        Customer phone: {phone},
     

        '''
        emailobj.sendMail()
        # response = requests.request("POST", url, data=payload)      

        # payload = {'From': 'cozysp', 'To': '7008975760',
        #            'TemplateName': 'Admin MSG', 'MSG': "Hi Jai, Customer Details Eswar, 9090909090"}

        # headers = {
        #             'Content-Type': 'multipart/form-data'
        #         }
        # response = requests.request("POST", url, data=payload, headers=headers)
        
    except Exception as e:
        print(e)
    # print(response.json())    
    # return JsonResponse(response.json())
    return JsonResponse({"message": "triggered"})


@api_view(["POST"])
@csrf_exempt
def contact_us_call(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')


        # url = f'https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/ADDON_SERVICES/SEND/TSMS'
                 
        # payload = {
        #     "From": "cozysp",
        #     "To": "7008975760,", 
        #     "TemplateName": "Admin MSG", 
        #     "VAR1":name, 
        #     "VAR2": email,
        #     "VAR3":subject, 
        #     "VAR4": msg,
        #     # "VAR5":name, 
        #     # "VAR6": phone
        #     }
 
        emailobj = EmailSending()
        emailobj.sub = subject
        # emailobj.to = 'avsr94@gmail.com'
        emailobj.body = f'''
        Name of Customer: {name},
        Customer Email: {email},
        Message: {msg}

        '''
        emailobj.sendMail()
        
    except Exception as e:
        print(e)
    # print(response.json())    
    # return JsonResponse(response.json())
    return JsonResponse({"message": "triggered"})
