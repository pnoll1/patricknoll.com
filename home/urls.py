from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^index', views.index, name='index'),
    re_path(r'edits', views.edits, name='edits'),
    re_path(r'resume', views.resume, name='resume'),
    re_path(r'^design', views.design, name='design'),
    re_path(r'^stress_analysis', views.stress_analysis, name='stress_analysis'),
    re_path(r'^3d_modeling', views.modeling, name='3d_modeling'),
    re_path(r'^programming', views.programming, name='programming'),
    re_path(r'^contact', views.contact, name='contact'),
    path('posts/<slug:slug>', views.posts)
]
