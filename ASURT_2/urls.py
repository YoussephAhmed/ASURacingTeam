from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^tickets/', include('ticketSys.urls',namespace='ticketSys', app_name='ticketSys')),
    url(r'^registeration/', include('registeration.urls', namespace='registeration', app_name='registeration')),

]


