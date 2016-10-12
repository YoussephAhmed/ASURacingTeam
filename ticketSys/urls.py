from django.conf.urls import url
from . import views

app_name = 'ticketSys'
urlpatterns = [
    url(r'^$', views.dashBoard, name='dashBoard'),

    url(r'^(?P<ticket_id>[0-9]+)/detail/$', views.detail, name='detail'),
    # url(r'^add/$', views.add, name='add'),

]
