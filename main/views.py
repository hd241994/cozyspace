import requests, urllib.parse
from .models import GetQoute
from .emailAPI import EmailSending
from cozyspace import settings
from django.http import response
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
	return render(request, 'main/index.html')


def form_1(request):
	try:
		request.session.flush()
		floorList = ['1 BHK', '2 BHK', '3 BHK', '3+ BHK']
		bhkList = ['New Project', 'Renovation']

		if request.method == 'POST':
			floortype = request.POST.get('floortype')
			bhktype = request.POST.get('bhktype')

			request.session['floortype'] = floortype
			request.session['bhktype'] = bhktype

			if (floortype in floorList) and (bhktype in bhkList):
				if bhktype == 'Renovation':
					return redirect('reno')
				return redirect('form_2')
			else:
				return render(request, 'form-1.html')
		else:
			return render(request, 'form-1.html')
	except Exception as e:
		print("Exception in form_1:",e)


def form_2(request):
	try:
		if request.method == "POST":
			request.session['kitchen'] = request.POST.get("kitchen")
			request.session['wardrobe'] = request.POST.get("wardrobe")
			request.session['crockery'] = request.POST.get("crockery")
			request.session['pooja room'] = request.POST.get("pooja room")
			request.session['study unit'] = request.POST.get("study unit")
			request.session['entmntunit'] = request.POST.get("entmntunit")
			request.session['washroom'] = request.POST.get("washroom")
			return redirect('form_3')
			
	except Exception as e:
		print("Exception in form_2:",e)
	return render(request, 'form-2.html')


def renovation(request):
	try:
		if request.method == 'POST':
			# print(request.POST)
			request.session['OwnerType'] = request.POST.get("ownertype", "ownertype")
			request.session['budget'] = request.POST.get("budget", "budget")
			request.session['possession'] = request.POST.get("possession", "Not Selected")
			return redirect('form_3')
		return render(request, 'form-renovation.html')
	except Exception as e:
		print("Exception in renovation:",e)



def pincode_validation(pin):
	try:
		postal_url = r'https://api.postalpincode.in/pincode/'+pin
		response = requests.request('GET', postal_url)
		response = response.json()
		pin_data = response[0]
		if pin_data['Status'] == "Success": # and pin_data['PostOffice'] != None:
			return True
		else:
			return False
	except Exception as e:
		print("Exception in pincode_validation:",e)


def form_3(request):
	import ipdb; ipdb.set_trace()
	try:
		if request.method == 'POST':
			pin = request.POST.get('pincode')
			# request.session['PIN'] = pin
			if pin != None and pin != '':
				pin_is_valid = pincode_validation(pin)
				if not pin_is_valid:
					return render(request, 'form-3.html')

				request.session['cutomer_phone'] = request.POST.get('phone')
				getObj = GetQoute()
				getObj.customer_name = request.POST.get('name', 'name')
				getObj.customer_email = request.POST.get('email', 'email')
				getObj.customer_number = request.POST.get('phone', 'phone')
				getObj.possesion_time = request.POST.get('possesionDate', '')
				getObj.pincode = pin
				getObj.reg_date = timezone.now()

				getObj.floorPlan = request.session['floortype']
				getObj.purpose = request.session['bhktype']

				if 'kitchen' in request.session:
					getObj.kitchen = request.session['kitchen']
					getObj.wardrobe = request.session['wardrobe']
					getObj.crockeryunit = request.session['crockery']
					getObj.poojaroom = request.session['pooja room']
					getObj.studyunit = request.session['study unit']
					getObj.entertainmentunit = request.session['entmntunit']
					getObj.entertainmentunit = request.session['washroom']

				if 'OwnerType' in request.session and \
					'budget' in request.session and \
						'possession' in request.session:
					getObj.ownertype = request.session['OwnerType']
					getObj.budget = request.session['budget']
					getObj.possesion_type = request.session['possession']
				getObj.save()

				emailobj = EmailSending()
				emailobj.sub = 'REQUEST A QUOTE'
				# emailobj.to = 'avsr94@gmail.com'
				emailobj.body = f'''
				Name of Customer: {request.POST.get('name')},
				Customer Number: {request.POST.get('phone')},
				Customer Email: {request.POST.get('email')},
				Customer Possesion Date:{request.POST.get('possesionDate', '')},
				Customer Pin:{pin},
				Floor Type:{request.session['floortype']},
				Purpose:{request.session['bhktype']},
				Kitchen:{request.session.get('kitchen', '')},
				Wardrobe:{request.session.get('wardrobe', '')},
				Crockery Unit:{request.session.get('crockery', '')},
				Pooja Room:{request.session.get('pooja room', '')},
				Study Unit:{request.session.get('study unit', '')},
				Entertainment Unit:{request.session.get('entmntunit', '')},
				Washroom:{request.session.get('washroom', '')},
				Owner Type:{request.session.get('OwnerType', '')},
				Budget:{request.session.get('budget', '')},
				Possession:{request.session.get('possession', '')},

				'''
				emailobj.sendMail()


				request.session['PIN'] = pin
				request.session['Name'] = request.POST.get('name', )
				request.session['Email'] = request.POST.get('email', 'email')
				request.session['Phone'] = request.POST.get('phone', 'phone')
				# request.session['Possession Date'] = request.POST.get('possesionDate', '')

				
				return redirect('send-otp')
				# return redirect('customer-list')
		else:
			return render(request, 'form-3.html')
	except Exception as e:
		print("Exception in form_3:",e)
	
	return render(request, 'form-3.html')


def send_otp(request):
	try:
		number = request.session['cutomer_phone']
		# url = f'https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/SMS/+91{number}/AUTOGEN'
		url = f'https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/SMS/+91{number}/AUTOGEN/OTP COZYSP'
		payload = ""
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		response = requests.request('GET', url, data=payload, headers=headers)
		response = response.json()
		# print(response)
		if response['Status'] == 'Success':
			request.session['session_id'] = response['Details']
			return redirect('otp-validation')
		else:
			return HttpResponse('You entered incorrect Phone Number.')
	except Exception as e:
		print(e)


def send_cust_details(request):
	try:
		url = f'https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/ADDON_SERVICES/SEND/TSMS'
		payload = {
					'From': 'cozysp',
					'To': '9059832520',
					'TemplateName': 'Admin MSG',
					'VAR1': f"{request.session['Name']}",
					'VAR2': f"{request.session['cutomer_phone']}",
					'VAR3': f"{request.session['PIN']}",
					'VAR4': f"{request.session['floortype']}",
					'VAR5': f"{request.session['bhktype']}",
					'VAR6': f"{request.session.get('budget', 'Budget')}"
					}

		headers = {
					'Content-Type': 'multipart/form-data'
				}
		# response = requests.request("POST", url, data=payload, headers=headers)
		subject = 'REQUEST A  QUOTE' 
		message = "Customer Details \n" + str(request.session['Name']) + ', \n' + str(request.session['cutomer_phone']) + ', \n' + \
					str(request.session['PIN']) + ', \n' + str(request.session['floortype']) + ', \n'+ str(request.session['bhktype'])+ \
					', \n' + request.session.get('budget', 'Budget')
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['deviprasaddigital@gmail.com', 'esu.b.tech@gmail.com']
		send_mail( subject, message, email_from, recipient_list ) 

		# requests.request()
	except Exception as e:
		print(e)


def otp_validation(request):
	try:
		if request.method == 'POST':
			user_otp = request.POST.get('otp', '')
			if user_otp:
				session_id = request.session['session_id']
				url = f'https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/SMS/VERIFY/{session_id}/{user_otp}'
				payload = ""
				headers = {'content-type': 'application/x-www-form-urlencoded'}

				response = requests.request("GET", url, data=payload, headers=headers)
				response = response.json()
				
				if response["Status"] == "Success":
					cust = GetQoute.objects.filter(customer_name=request.session['Name'], 
						customer_email=request.session['Email']).last()
					cust.is_number_verified = True
					cust.save()
					# send_cust_details(request)
					request.session.flush()
					return HttpResponse("Thanks for registering here.")
				else:
					return HttpResponse("OTP Mismatched!!!!")
		
	except Exception as e:
		print("Exception in otp_validation:",e)
	
	return render(request, 'otp-validation.html')



def customers_list(request):
	customer_list = None
	page_obj = None
	try:
		customer_list = GetQoute.objects.all()[::-1]
		paginator = Paginator(customer_list, 10)
		page = request.GET.get('page')
		page_obj = paginator.get_page(page)
	except Exception as e:
		print(e)
	return render(request, 'customerdetails.html', {'customers': page_obj})


def customer_detail(request, pk):
	return render(request, 'customer.html', {'customer': get_object_or_404(GetQoute, pk=pk)})

def delete_customer(request, pk):
	try:
		customer = GetQoute.objects.get(pk=pk)
		customer.delete()
		return redirect('customer-list')
	except Exception as e:
		print(e)

def registred_response(request):
		return render(request, 'main/registred.html')
