from django.http import HttpResponse, FileResponse
from django.template import Context,loader
from django.shortcuts import render
import psycopg2
from collections import OrderedDict
from .models import post
import json
import os


def index(request):
    context = {}
    posts = {}
    context['static'] = '/static'
    context['posts'] = post.objects.all()
    return render(request, 'index.html',context)
def edits(request):
    # server cant find file without fullpath
    edits = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static/data.geojson')
    # file only load in binary mode
    return FileResponse(open(edits, 'rb'))
def resume(request):
    context_resume = {}
    project =   {'name':'patricknoll.com','technologies':'JS','startdate':'20190411','enddate':'20190412', 'responsibilities':'Create responsive portfolio website using bootstrap  framework'}
    projects = {}
    projects['patricknoll.com'] = project
    context_resume['static'] = '/static'
    context_resume['projects'] = projects
    return render(request, 'resume.html',context_resume)
