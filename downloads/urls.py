from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('downloads', views.downloads),
    re_path(r'^downloads/static',views.serve_downloads),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('register', views.register),
    path('payment', views.payment),
    path('webhooks', views.webhook_view),
]
