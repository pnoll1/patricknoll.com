from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    re.path(r'^$', views.index, name='index'),
    re.path(r'^index', views.index, name='index'),
    re.path(r'^services', views.services, name='services'),
    re.path(r'edits', views.edits, name='edits'),
    re.path(r'resume', views.resume, name='resume'),
    re.path(r'^design', views.design, name='design'),
    re.path(r'^stress_analysis', views.stress_analysis, name='stress_analysis'),
    re.path(r'^3d_modeling', views.modeling, name='3d_modeling'),
    re.path(r'^programming', views.programming, name='programming'),
    re.path(r'^contact', views.contact, name='contact'),
    path('posts/<slug:slug>', views.posts)
]
