from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'edits', views.edits, name='edits'),
    url(r'resume', views.resume, name='resume')
]
