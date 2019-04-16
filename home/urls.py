from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'edits', views.edits, name='edits'),
    url(r'resume', views.resume, name='resume'),
    url(r'^design', views.design, name='design'),
    url(r'^stress_analysis', views.stress_analysis, name='stress_analysis'),
    url(r'^3d_modeling', views.modeling, name='3d_modeling'),
    url(r'^programming', views.programming, name='programming'),
]
