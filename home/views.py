from django.http import HttpResponse, FileResponse
from django.template import Context,loader
from django.shortcuts import render
from collections import OrderedDict
from .models import post, project, position
import os
from django.core.paginator import Paginator

#posts = {}
def index(request):
    context = {}
    if request.GET.get('expand_map') == 'yes':
        context['expand_map'] = 'yes'
    context['static'] = '/static'
    page = request.GET.get('page')
    post_list = post.objects.all()
    paginator = Paginator(post_list,5)
    posts = paginator.get_page(page)
    context['posts'] = posts
    return render(request, 'index.html',context)
def edits(request):
    # server cant find file without fullpath
    edits = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static/data.geojson')
    # file only load in binary mode
    return FileResponse(open(edits, 'rb'))
def resume(request):
    context_resume = {}
    context_resume['static'] = '/static'
    if request.GET.get('q') == 'software':
        context_resume['projects'] = project.objects.all()
    else:
        context_resume['position'] = position.objects.all()
    return render(request, 'resume.html',context_resume)
def design(request):
    context = {}
    context['static'] = '/static'
    return render(request, 'design.html', context)
def stress_analysis(request):
    context = {}
    context['static'] = '/static'
    return render(request, 'stress_analysis.html', context)
def modeling(request):
    context = {}
    context['static'] = '/static'
    return render(request, '3d_modeling.html', context)
def programming(request):
    context = {}
    context['static'] = '/static'
    return render(request, 'programming.html', context)
