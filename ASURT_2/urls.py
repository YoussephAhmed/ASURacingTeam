# this file roots the URLconf at the .urls files in each
# app to the URLconf of the project which is in this file

# When somebody requests a page from the website
# Django will load the this
# Python module because it is pointed to by the ROOT_URLCONF setting


from django.conf.urls import url, include
from django.contrib import admin
from ticketSys.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),

    # The include() function allows referencing other URLconfs
    # it chops off whatever part of the URL matched up to that point
    # and sends the remaining string to the included URLconf for further processing.

    # defining the apps URL
    # /tickets/
    url(r'^tickets/', include('ticketSys.urls', namespace='ticketSys', app_name='ticketSys')),

    # /registeration/
    url(r'^registeration/', include('registeration.urls', namespace='registeration', app_name='registeration')),

    # /foreignClubs/
    url(r'^foreignClubs/', include('foreignClubs.urls', namespace='foreignClubs', app_name='foreignClubs')),

    # /events/
    url(r'^events/', include('events.urls', namespace='events', app_name='events')),

    # Default page to access all the work (DEVELOPMENT ONLY)
    url(r'^$', index, name='index'),

]
