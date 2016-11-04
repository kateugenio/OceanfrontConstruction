from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
	# request.session.pop('emailConfirm', None)

	return render(request, 'ofc/index.html')


def contact(request):
	firstName = request.POST['first_name']
	lastName = request.POST['last_name']
	email = request.POST['email']
	phone = request.POST['contactnum']
	clientMsg = request.POST['client_text']
	from_email = settings.EMAIL_HOST_USER
	to_email = settings.EMAIL_HOST_USER
	send_mail('A message from your visitor: '+firstName +' '+lastName, 'Here is the message: '+ clientMsg, from_email,
    ['kateugenio425@gmail.com'], fail_silently=False, html_message="Email: " + email + "\n" + "Phone: " + phone + "\n" + "Message: " + clientMsg + "\n")
    	messages.add_message(request, messages.SUCCESS, 'Thank you for submitting your information, we will contact you shortly.')
	# request.session['emailConfirm'] = "Thank you for submitting your information, we will contact you shortly"
	return redirect('/#contact')
