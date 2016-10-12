from django.conf.urls import include, url
from . import views

from registeration.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login_user/$', views.login_user, name = 'login_user'),
    url(r'^logout_user/$',views.logout_user, name = 'logout_user'),
]