from urllib.error import HTTPError
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import random
import string
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
User = get_user_model()
from app.models import userdetail, RECOVERY, RETURNS, order
from datetime import datetime


length = 6
randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=length))

def send_activation_email(user, request):
	current_site = get_current_site(request)
	email_subject = "Activate Your Account"
	email_body = render_to_string('mail/activation.html', {
		'user': user,
		"domain": current_site,
		"username": urlsafe_base64_encode(force_bytes(user.username)),
		"token": user.phrase
	})
	email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_FROM_USER, 
	to=[user.email])
	email.send()

def activate_user(request, username, token):
	try:
		uid = force_str(urlsafe_base64_decode(username))
		user = User.objects.get(username=uid)
	except Exception as e:
		user = None

	if user and user.phrase == token:
		user.is_verified = True
		user.save()
		return redirect('/signin/')
	return HttpResponse('Failed')





@login_required(login_url='/signin/', redirect_field_name=None)
def logoutview(request):
	logout(request)
	messages.add_message(request, messages.ERROR, 'Logout Successfully')
	return redirect('/signin/')



def signin(request):
	if request.method == 'POST':
		email = str(request.POST.get('useremail')).lower()
		password = request.POST.get('password')
		user = authenticate(request, username=email, password=password)
		if user is not None:
			if user.is_verified:
				login(request, user)
				return redirect('/')
			else:
				messages.add_message(request, messages.ERROR, mark_safe('Your Account Is Not Verified, Please Check Your &nbsp<a class="btn btn-outline-warning" href="https://gmail.com" target="_blanck">Gmail</a> Inbox Or Spam'))
				send_activation_email(user, request)
				return render(request, 'user/signin.html')
		else:
			messages.add_message(request, messages.ERROR, 'Invalid Credentials')
			return render(request, 'user/signin.html')
	return render(request, 'user/signin.html')


def signup(request):
	if request.method == 'POST':
		username = str(request.POST['username']).lower()
		email = str(request.POST['email']).lower()
		pass1 = request.POST['password']
		data = True
		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.ERROR, mark_safe('Username Already Exists, Please Try To &nbsp<a class="btn btn-outline-warning" href="/signin/">Signin</a>'))
			data = False
		if User.objects.filter(email=email).exists():
			messages.add_message(request, messages.ERROR, mark_safe('Email Already Exists, Please Try To &nbsp<a class="btn btn-outline-warning" href="/signin/">Signin</a>'))
			data = False
		if data:
			user = User.objects.create_user(username=username, email=email, password=pass1)
			user.phrase = randomstr
			user.save()
			send_activation_email(user, request)
			return render(request, "user/verificationsent.html")
		else:
			return render(request, 'user/signup.html')
	# messages.add_message(request, messages.ERROR, 'Done')
	return render(request, 'user/signup.html')




def send_forget_email(user, request):
	current_site = get_current_site(request)
	email_subject = "Reset Your Account Password"
	email_body = render_to_string('mail/reset.html', {
		'user':user,
		"domain":current_site,
		"username":urlsafe_base64_encode(force_bytes(user.username)),
		"token":user.phrase
	})
	email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_FROM_USER, 
	to=[user.email])
	email.send()

def reset_user(request, username, token):
	try:
		uid = force_str(urlsafe_base64_decode(username))
		user = User.objects.get(username=uid)
	except Exception as e:
		user = None

	if user and user.phrase == token:
		user.is_verified = True
		user.save()
		return render(request, 'user/newpassword.html', {"user":user.username})
	return HttpResponse('Failed')




def forget(request):
	if request.method=='POST':
		email = request.POST['email']
		if User.objects.filter(email=email).exists:
			user = User.objects.get(email=email)
			send_forget_email(user, request)
			return redirect("/reset-sent/")
		else:
			messages.add_message(request, messages.ERROR, 'Email Does\'nt Exists')
			return render(request, 'user/forget.html')
	return render(request, 'user/forget.html')


def new_password(request):
	if request.method == 'POST':
		newpass = request.POST['password']
		users = request.POST['user']
		user = User.objects.get(username=users)
		user.set_password((str(newpass)))
		user.save()
		messages.add_message(request, messages.ERROR, 'Password Reset Successfully')
		return redirect('/signin/')
	return render(request, 'new-password.html')

def verification(request):
	return render(request, 'user/verificationsent.html')


def resest_send(request):
	return render(request, 'user/forgetsent.html')
