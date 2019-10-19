from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import FileResponse
from .models import *
import datetime
import os
import stripe
import re

def create_checkout_session(request):
    stripe.checkout.Session.create(
      payment_method_types=['card'],
      client_reference_id= request.user.username,
      line_items=[{
        'name': 'US Maps for OSMAnd',
        'description': "State Maps for OSMAnd with millions of addresses added, You'll receive updates monthly for the next 12 months",
        'amount': 1000,
        'currency': 'usd',
        'quantity': 1,
      }],
      success_url='http://localhost:8002/downloads?session_id={CHECKOUT_SESSION_ID}',
      cancel_url='http://localhost:8002/downloads',
    )

# timezone class
class Utc(datetime.tzinfo):
    _offset = datetime.timedelta(hours=0)
    _dst = datetime.timedelta(0)
    def utcoffset(self,dt):
        return self.__class__._offset
    def dst(self, dt):
        return self.__class__._dst

utc = Utc()

def downloads(request):
    context = {}
    context['static'] = '/static'
    # check user is logged in and has valid subscription
    if request.user.is_authenticated and request.user.subscription.end_date > datetime.datetime.now(utc):
        file_names = os.listdir('./downloads/static/downloads')
        context['files'] = file_names
        return render(request, 'downloads.html', context)
    else:
        return redirect('/login')

def serve_downloads(request):
    if request.user.is_authenticated and request.user.subscription.end_date > datetime.datetime.now(utc):
        file_name = request.path.split('/')[-1]
        file_path = os.path.join('downloads/static/downloads/' + file_name)
        return FileResponse(open(file_path, 'rb'))
    else:
        messages.error(request, "Must be logged in with valid subscription")
        return redirect('/')

def login_view(request):
    context = {}
    context['static'] = '/static'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    # Successfull login
    if user is not None and request.method == 'POST':
        login(request, user)
        messages.success(request, 'Login Successfull')
        return redirect('/downloads')
    # redirect logged in user
    elif request.user.is_authenticated and request.method == 'GET':
        messages.info(request, "You're already logged in")
        return redirect('/')
    # login not yet tried
    elif request.method == 'GET' and user is None:
        return render(request, 'login.html',context)
    # failed login
    else:
        messages.error(request, 'Login Failed')
        return render(request, 'login.html',context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfull')
    return redirect('/')

def register(request):
    context = {}
    context['static'] = '/static'
    # check if form views be better
    #first_name = request.POST.get('first_name')
    #last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirm = request.POST.get('password_confirm')
    invite_code = request.POST.get('invite_code')
    if username and email and password and password_confirm:
        if password != password_confirm:
            messages.error(request,"The password fields must match")
        # user registration handling
        user = User(username=username, email=email, password=password)
        try:
            user.full_clean()
        except ValidationError as e:
            messages.error(request,e)
            return render(request, 'register.html',context)
        if not User.objects.filter(username=username):
            User.objects.create_user(username=username, email=email, password=password) #, is_active=False
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, 'Username reserved, Redirecting to payment')
            return redirect('/payment')
        messages.error(request, 'Username taken')
    else:
        messages.error(request, 'Fields missing')
    # send confirmation email
    return render(request, 'register.html',context)

def payment(request):
    context = {}
    context['static'] = '/static'
    if request.user.is_authenticated:
        #session = create_checkout_session(request)
        session = stripe.checkout.Session.create(
              payment_method_types=['card'],
              client_reference_id= request.user.username,
              line_items=[{
                'name': 'US Maps for OSMAnd',
                'description': "State Maps for OSMAnd with millions of addresses added, You'll receive updates monthly for the next 12 months",
                'amount': 1000,
                'currency': 'usd',
                'quantity': 1,
              }],
              success_url='https://localhost:8002/downloads?session_id={CHECKOUT_SESSION_ID}',
              cancel_url='https://localhost:8002/downloads',
            )
        context['CHECKOUT_SESSION_ID'] = session.id
        return render(request, 'payment.html', context)
    else:
        return redirect('/login')

# Using Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# You can find your endpoint's secret in your webhook settings
endpoint_secret = 'whsec_...'

@csrf_exempt
def webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    def handle_checkout_session(session):
        user = User.objects.get(session.client_reference_id)
        user.subscription.end_date = datetime.datetime.now(utc) + datetime.timedelta(days=365)
        try:
            user.full_clean()
        except ValidationError as e:
            pass
        user.save()
    handle_checkout_session(session)

  return HttpResponse(status=200)
