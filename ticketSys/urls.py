from django.conf.urls import url
from . import views

app_name = 'ticketSys'
urlpatterns = [
    # /tickets/
    url(r'^$', views.dashBoard, name='dashBoard'),

    # /tickets/add/
    url(r'^add/', views.TicketCreate.as_view(), name='add_ticket'),

    # /tickets/123/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    # /tickets/123/addcomment/
    url(r'^(?P<pk>[0-9]+)/addcomment/$', views.addComment, name='add_comment'),
]
