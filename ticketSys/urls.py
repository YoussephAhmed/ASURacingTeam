# this is a simple mapping between URL patterns(simple regular expressions) to
# Python functions(views).

from django.conf.urls import url
from . import views

# to namespace this urlpatterns
app_name = 'ticketSys'
# make a function that checks whether the user is an authenticated ticket member and call it in every url
urlpatterns = [
    # /tickets/
    url(r'^$', views.dashBoard, name='dashBoard'),

    # /tickets/add/
    url(r'^add/', views.addTicket, name='add_ticket'),

    # /tickets/123/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    # /tickets/123/addcomment/
    url(r'^(?P<pk>[0-9]+)/addcomment/$', views.addComment, name='add_comment'),

    # /tickets/123/changestate/
    url(r'^(?P<pk>[0-9]+)/changestate/$', views.changeState, name='change_state'),

    # /tickets/login/
    url(r'^login/', views.login, name='login'),
    # /chooseRTMember//
    url(r'^chooseRTMember/', views.chooseRTMember, name='choose_RTMember'),
    # /RTMemberAdded/
    url(r'^RTMemberAdded/$', views.addRTMember, name='RTMember_Added'),

    # /testAjax/
    url(r'^testAjax/$', views.testAjax, name='test_ajax'),

]
