from django.conf.urls import url
from . import views

# to namespace this urlpatterns
app_name = 'events'
# make a function that checks whether the user is an authenticated ticket member and call it in every url
urlpatterns = [
    # /events/organizers/
    url(r'^organizers/$', views.organizers, name='organizers'),
]
