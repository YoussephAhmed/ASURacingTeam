from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rtMembers.models import RTMember, Roles
from ticketSys.models import TicketMember, TicketComment, Ticket, States
from django.contrib.auth.models import User
from django.db.models import Q
from ticketSys import emailSender
from django.contrib.auth import authenticate, login
from django.core.files.base import ContentFile


# detail get called like this
# detail(request=<HttpRequest object>, question_id='34')
# question_id='34' from (?P<pk>[0-9]+)/ part of the URL

def isAuthTicketMember(request):
    if request.user.is_authenticated():
        if isTicketMember(request.user):
            return True
    return False


def isTicketMember(user):
    try:
        if getTicketMemberFromUser(user) is not None:
            return True
    except:
        return False
    return False


# it gets all the details about a specified ticket and render it to the template
def detail(request, pk):
    if not isAuthTicketMember(request):  # continue if only the user is a TicketMember
        return redirect('registeration:index')
    # Get the ticket related with the pk from the database or rise an 404 error if it is not found
    ticket = get_object_or_404(Ticket, pk=pk)
    # Get the comments related to the Ticket to be displayed in the details template
    comms = TicketComment.objects.filter(ticketid_id=pk)
    # States.STATES is to get the tuble in class States that holds all the possible states
    context = {'ticket': ticket, 'comments': comms, 'states': States.STATES}
    # Send too the template
    return render(request, 'ticketSys/detail.html', context)


def addComment(request, pk):  # add comment to the ticket detail page
    if not isAuthTicketMember(request):  # continue if only the user is a TicketMember
        return redirect('registeration:index')
    comment = request.POST['comment']
    user = request.user
    tm = getTicketMemberFromUser(user)
    ticket = Ticket.objects.get(id=pk)
    comm = TicketComment(memberid=tm, ticketid=ticket, comment=comment)
    comm.save()
    return redirect('ticketSys:detail', pk)


def changeState(request, pk):
    if not isAuthTicketMember(request):  # continue if only the user is a TicketMember
        return redirect('registeration:index')
    s = request.POST['state']
    t = Ticket.objects.get(id=pk)
    # check if the member able to change the state of the ticket
    # if state was  'waiting_it'
    # the IT members or All heads only can be able to change the state
    # NOTE any Managerial head begin with X
    # (0, 'WAITING_HR'), (1, 'WAITING_IT'), (2, 'WAITING'), (3, 'SOLVED')
    if t.state is not s:
        domain = request.META['HTTP_HOST']
        emailRelatedMembers(s, pk, domain)  # to notify who should be notified by email or whatever
        t.state = s
        t.save()

    return redirect('ticketSys:detail', pk)


#  login form
#  data about the ticket in the mail
# todo add image

# todo don't show RTMembers in the user list
# todo can search for the user
class TicketCreate(CreateView):# this class is attached to the file Ticket_form.html and also form_template.html
    model = Ticket
    fields = ['userid', 'title', 'content']  # member id should be taken from the logged in user

    def form_valid(self, form):
        ticket = form.save(commit=False)
        domain = self.request.META['HTTP_HOST']

        try:
            self.request.POST['needhr']
            # Need HR approval
            ticket.state = 0
            emailHR(ticket.id, domain)
        except:  # Does not need HR approval
            ticket.state = 1
            emailIT(ticket.id, domain)

        user = self.request.user
        try:
            ticket.memberid = getTicketMemberFromUser(user)
        except:
            return redirect('ticketSys:dashBoard')
        return super(TicketCreate, self).form_valid(form)


# todo only send emails for members in the TicketMembers
# send emails to the RTMembers with role HR
def emailHR(pk, domain):
    rtMembers = RTMember.objects.filter(
        Q(role=2) | Q(role=3) | Q(role=4) | Q(role=5))  # the indices of the HR(OD,REC) in ROLES
    for rtMember in rtMembers:
        receiver = getUserFromRTMember(rtMember)
        if receiver.email is not '' and receiver.email is not None and receiver.email != '':
            emailSender.autoMailSender(receiver.email, pk, domain)


# todo only send emails for members in the TicketMembers
# send emails to the RTMembers with role IT
def emailIT(pk, domain):
    rtMembers = RTMember.objects.filter(Q(role=0) | Q(role=1))  # the indices of the IT in ROLES
    for rtMember in rtMembers:
        receiver = getUserFromRTMember(rtMember)
        if receiver.email is not '' and receiver.email is not None and receiver.email != '':  # todo this lets empty emails get to the function solve that
            emailSender.autoMailSender(receiver.email, pk, domain)


# email the member associated with the change depending on his/her role
def emailRelatedMembers(state, pk, domain):
    # (0, 'WAITING_HR'), (1, 'WAITING_IT'), (2, 'WAITING'), (3, 'SOLVED')
    if state == '0':  # handling state 0 -> HR
        emailHR(pk, domain)

    elif state == '1':  # handling state 1 -> IT
        emailIT(pk, domain)

    elif state == '2':  # send email to the ticket starter
        ticket = Ticket.objects.get(id=pk)
        ticketmember = TicketMember.objects.get(id=ticket.memberid_id)
        rtMember = RTMember.objects.get(id=ticketmember.memberid_id)
        receiver = getUserFromRTMember(rtMember)
        if receiver.email is not '' and receiver.email is not None and receiver.email != '':
            emailSender.autoMailSender(receiver.email, pk, domain)


def dashBoard(request):
    if not isAuthTicketMember(request):  # continue if only the user is a TicketMember
        return redirect('registeration:index')
    tickets = Ticket.objects.all()  # get all the tickets in the database
    context = {'tickets': tickets}
    return render(request, 'ticketSys/dashboard.html', context)  # send it to the template


# returns the TicketMember associated with that User
def getTicketMemberFromUser(user):
    rtmember = RTMember.objects.get(userid_id=user.id)
    return TicketMember.objects.get(memberid_id=rtmember.id)


# returns the User associated with that RTMember
def getUserFromRTMember(rtMember):
    memberID = rtMember.userid.id
    return User.objects.get(id=memberID)


#related to Comment Images

#
# def save_file(request):
# 	mymodel = CommentImg.objects.get(id=1)
# 	file_content = ContentFile(request.FILES['video'].read())
# 	mymodel.video.save(request.FILES['video'].name, file_content)