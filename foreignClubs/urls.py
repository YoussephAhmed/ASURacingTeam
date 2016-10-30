from django.conf.urls import url
from . import views

# to namespace this urlpatterns
app_name = 'foreignClubs'
# make a function that checks whether the user is an authenticated ticket member and call it in every url
urlpatterns = [
    # /foreignClubs/heads/
    url(r'^heads/$', views.heads, name='heads'),
]
