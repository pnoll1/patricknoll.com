# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import post

class ViewTests(TestCase):
    def setUp(self):
        p = post(slug='Low-Volume-Production-With-3D-Printing', date='2019-01-13', md_content='''I bought a Prusa i3 MK3 3D printer to do some prototyping and low volume production. After doing some rapid prototyping, I came up with a product for organizing dewalt batteries. The polished dual iteration is pictured below.

![image](/static/images/isometric no battery inside.jpg)

 The product was designed using parametric models in FreeCAD, stress calcs and costing with python, sliced with Slic3r PE, ran with Printrun or Octoprint all on a Debian desktop. Production went smooth until the printer became increasingly erratic on the first layer. Overall, 3D printing could be a viable production method if you can get hobby pricing AND reliability. Reliability still needs work.

A full report on the design can be found in my mechanical portfolio.''')
        p.save()

    def test_paths(self):
        c = Client()
        r = c.get('http://localhost:8000')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/contact')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/services')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/boogaliboo')
        self.assertEqual(r.status_code, 404)
        r = c.get('http://localhost:8000/posts/boogaliboo')
        self.assertEqual(r.status_code, 404)
        r = c.get('http://localhost:8000/posts/Low-Volume-Production-With-3D-Printing')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/resume')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/resume?q=software')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/resume?q=mechanical')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/design')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/stress_analysis')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/3d_modeling')
        self.assertEqual(r.status_code, 200)
        r = c.get('http://localhost:8000/programming')
        self.assertEqual(r.status_code, 200)
