from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rtMembers.models import RTMember, Roles
from ticketSys.models import TicketMember, TicketComment, Ticket, States
from django.contrib.auth.models import User
from django.db.models import Q
from ticketSys import emailSender


def detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    comms = TicketComment.objects.filter(ticketid_id=pk)
    context = {'ticket': ticket, 'comments': comms, 'states': States.STATES}

    return render(request, 'ticketSys/detail.html', context)


def addComment(request, pk):#add comment to the ticket detail page
    comment = request.POST['comment']
    user = request.user
    tm = getTicketMemberFromUser(user)
    ticket = Ticket.objects.get(id=pk)
    comm = TicketComment(memberid=tm, ticketid=ticket, comment=comment)
    comm.save()
    return redirect('ticketSys:detail', pk)


def changeState(request, pk):
    s = request.POST['state']
    t = Ticket.objects.get(id=pk)
    # check if the member able to change the state of the ticket
    # if state was  'waiting_it'
    # the IT members or All heads only can be able to change the state
    # NOTE any Managerial head begin with X
    # (0, 'WAITING_HR'), (1, 'WAITING_IT'), (2, 'WAITING'), (3, 'SOLVED')
    if t.state is not s:
        emailRelatedMembers(s, pk)  # to notify who should be notified by email or whatever
        t.state = s
        t.save()

    return redirect('ticketSys:detail', pk)


# todo don't show RTMembers in the user list
# todo can search for the user
class TicketCreate(CreateView):
    model = Ticket
    fields = ['userid', 'title', 'content']  # member id should be taken from the logged in user

    def form_valid(self, form):
        ticket = form.save(commit=False)
        try:
            self.request.POST['needhr']
            # Need HR approval
            ticket.state = 0
            emailHR()
        except:  # Does not need HR approval
            ticket.state = 1
            emailIT()

        user = self.request.user
        try:
            ticket.memberid = getTicketMemberFromUser(user)
        except:
            return redirect('ticketSys:dashBoard')
        return super(TicketCreate, self).form_valid(form)


# todo only send emails for members in the TicketMembers
def emailHR():
    rtMembers = RTMember.objects.filter(
        Q(role=2) | Q(role=3) | Q(role=4) | Q(role=5))  # the indices of the HR(OD,REC) in ROLES
    for rtMember in rtMembers:
        receiver = getUserFromRTMember(rtMember)
        if receiver.email is not None:
            emailSender.autoMailSender(receiver.email)


# todo only send emails for members in the TicketMembers
def emailIT():
    rtMembers = RTMember.objects.filter(Q(role=0) | Q(role=1))  # the indices of the IT in ROLES
    for rtMember in rtMembers:
        receiver = getUserFromRTMember(rtMember)
        if receiver.email is not None:
            emailSender.autoMailSender(receiver.email)


def emailRelatedMembers(state, pk):
    # (0, 'WAITING_HR'), (1, 'WAITING_IT'), (2, 'WAITING'), (3, 'SOLVED')
    if state == '0':  # handling state 0 -> HR
        emailHR()

    elif state == '1':  # handling state 1 -> IT
        emailIT()

    elif state == '2':  # send email to the ticket starter
        ticket = Ticket.objects.get(id=pk)
        ticketmember = TicketMember.objects.get(id=ticket.memberid_id)
        rtMember = RTMember.objects.get(id=ticketmember.memberid_id)
        receiver = getUserFromRTMember(rtMember)
        if receiver.email is not None:
            emailSender.autoMailSender(receiver.email)


def dashBoard(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'ticketSys/dashboard.html', context)


def getTicketMemberFromUser(user):  # returns the TicketMember associated with that User
    rtmember = RTMember.objects.get(userid_id=user.id)
    return TicketMember.objects.get(memberid_id=rtmember.id)


def getUserFromRTMember(rtMember):  # returns the User associated with that RTMember
    memberID = rtMember.userid.id
    return User.objects.get(id=memberID)
