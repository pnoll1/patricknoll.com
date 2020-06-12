# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import subscriptionFix
from django.contrib.auth.models import User
import datetime
from downloads.views import Utc

utc = Utc()

class ViewTests(TestCase):
    def setUp(self):
        # user with subscription
        username = 'pat'
        email = 'pat@patricknoll.com'
        password = 'password'
        user = User(username=username, email=email, password=password)
        User.objects.create_user(username=username, email=email, password=password)
        #give subscription
        s = subscriptionFix.objects.create(user='pat', end_date=datetime.datetime.now(utc) + datetime.timedelta(days=365))
        s.save()
        
        # user without subscription
        username = 'deadbeat'
        email = 'pat@patricknoll.com'
        password = 'password'
        user = User(username=username, email=email, password=password)
        User.objects.create_user(username=username, email=email, password=password)


    def test_paths(self):
        c = Client()
        r = c.get('http://localhost:8000/login')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/logout')
        self.assertEqual(r.status_code, 302)
        r = c.get('http://localhost:8000/register')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/downloads')
        self.assertEqual(r.status_code, 302)
        c = Client()
        # check login works
        r = c.post('/login', {'username':'pat', 'password':'password'}, follow=True)
        self.assertContains(r, 'Login Successfull')
        # check subscription works
        r = c.get('http://localhost:8000/downloads')
        self.assertEqual(r.status_code, 200)
        # logged in user can log out
        r = c.get('/logout', follow=True)
        self.assertContains(r, 'Logout Successfull')
        # user without subscription gets redirected
        r = c.post('/login', {'username':'deadbeat', 'password':'password'}, follow=True)
        self.assertContains(r, 'Need valid subscription')

