# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import requests

class ViewTests(TestCase):
    def test_paths(self):
        r = requests.get('http://localhost:8000')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/#contact')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/boogaliboo')
        self.assertEqual(r.status_code, 404)
        r = requests.get('http://localhost:8000/resume')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/resume?q=software')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/resume?q=mechanical')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/design')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/stress_analysis')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/3d_modeling')
        self.assertEqual(r.status_code, 200)
        r = requests.get('http://localhost:8000/programming')
        self.assertEqual(r.status_code, 200)
