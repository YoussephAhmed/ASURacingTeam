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
    comms = TicketComment.objects.filter(ticket_id=pk)
    # States.STATES is to get the tuble in class States that holds all the possible states
    context = {'ticket': ticket, 'comments': comms, 'states': States.STATES}
    return render(request, 'ticketSys/detail.html', context)  # Send to the template


def addComment(request, pk):  # add comment to the ticket detail page
    if not isAuthTicketMember(request):  # continue if only the user is a TicketMember
        return redirect('registeration:index')
    comment = request.POST['comment']
    user = request.user
    tm = getTicketMemberFromUser(user)
    ticket = Ticket.objects.get(id=pk)
    comm = TicketComment(ticketMember=tm, ticket=ticket, comment=comment)
    comm.save()
    return render(request, 'ticketSys/comment.html', {'com': comm})


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
#  add image
#  don't show RTMembers in the user list
#  can search for the user
#  change to function and fix error
def addTicket(request):
    if not isAuthTicketMember(request):  # continue if only the user is a TicketMember
        return redirect('registeration:index')

    if request.method == "GET":  # the user is entering the addTicket page, just view the page
        users = User.objects.filter(rtMember=None)  # get all users that are not RTMembers
        context = {'users': users}
        return render(request, 'ticketSys/addTicket.html', context)

    else:  # the user has submitted the form, validate the data
        try:
            ticketMember = getTicketMemberFromUser(request.user)
            userid = request.POST['selectedUser']
            user = User.objects.get(id=userid)
            try:  # fetch the state of the ticket
                request.POST['needhr']
                # Need HR approval
                state = 0
            except:  # Does not need HR approval
                state = 1

            title = request.POST['title']
            content = request.POST['content']
            if len(title) < 2 or len(content) < 2:  # validate that the title and content are not empty

                return redirect('ticketSys:add_ticket')

            ticket = Ticket(ticketMember=ticketMember, user=user, state=state, title=title, content=content)
            ticket.save()
            domain = request.META['HTTP_HOST']
            try:  # send emails to the concerned ticketMembers
                if state == 0:
                    emailHR(ticket.id, domain)
                else:
                    emailIT(ticket.id, domain)
            except:
                print('Error while emailing')

        except:
            redirect('ticketSys:add_ticket')

    return redirect('ticketSys:dashBoard')


# send emails to the RTMembers with role HR
def emailHR(pk, domain):
    rtMembers = RTMember.objects.filter(
        Q(role=2) | Q(role=3) | Q(role=4) | Q(role=5))  # the indices of the HR(OD,REC) in ROLES
    for rtMember in rtMembers:
        if isTicketMember(rtMember.user):
            receiver = getUserFromRTMember(rtMember)
            if receiver.email is not '' and receiver.email is not None and receiver.email != '':
                emailSender.autoMailSender(receiver.email, pk, domain)


# send emails to the RTMembers with role IT
def emailIT(pk, domain):
    rtMembers = RTMember.objects.filter(Q(role=0) | Q(role=1))  # the indices of the IT in ROLES
    for rtMember in rtMembers:
        if isTicketMember(rtMember.user):
            receiver = getUserFromRTMember(rtMember)
            if receiver.email is not '' and receiver.email is not None and receiver.email != '':  # this lets empty emails get to the function solve that
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
        ticketmember = TicketMember.objects.get(id=ticket.ticketMember_id)
        rtMember = RTMember.objects.get(id=ticketmember.rtMember_id)
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
    rtmember = RTMember.objects.get(user=user)
    return TicketMember.objects.get(rtMember=rtmember)


# returns the User associated with that RTMember
def getUserFromRTMember(rtMember):
    memberID = rtMember.user.id
    return User.objects.get(id=memberID)


# returns the RTMember related to the user
def getRTMemberFromUser(request):
    user = request.user
    rtMember = RTMember.objects.get(user=user.id)
    return rtMember


#  use this function to enble and disable a button in the system
def isRTMemberHead(rtMember):
    if rtMember.role == 1 or rtMember.role == 3 or rtMember.role == 5 or rtMember.role == 7 or rtMember.role == 9:
        return True

    return False


# related to Comment Images

#
# def save_file(request):
# 	mymodel = CommentImg.objects.get(id=1)
# 	file_content = ContentFile(request.FILES['video'].read())
# 	mymodel.video.save(request.FILES['video'].name, file_content)


def chooseRTMember(request):
    rtMember = getRTMemberFromUser(request)
    if isRTMemberHead(rtMember):
        context = {'users': User.objects.all(), 'roles': Roles.ROLES}
        return render(request, 'ticketSys/addRTMember.html', context)
    else:
        return redirect('registeration:index')


def addRTMember(request):
    user = request.POST['user']
    roleOfRTMember = request.POST['role']
    normalUser = User.objects.get(id=user)
    rtMember = RTMember(user=normalUser, role=roleOfRTMember)
    rtMember.save()
    return redirect('ticketSys:choose_RTMember')


def index(request):  # Used for DEVELOPMENTAL use only to make our lives easier shows shortcuts at the 1st page
    return render(request, 'ticketSys/index.html')
