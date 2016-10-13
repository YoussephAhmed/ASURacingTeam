from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rtMembers.models import RTMember
from ticketSys.models import TicketMember, TicketComment, Ticket, States
from django.contrib.auth.models import User


def detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    comms = TicketComment.objects.filter(ticketid_id=pk)
    context = {'ticket': ticket, 'comments': comms, 'states': States.STATES}

    return render(request, 'ticketSys/detail.html', context)


def addComment(request, pk):
    comment = request.POST['comment']
    user = request.user
    tm = getTicketMember(user)
    ticket = Ticket.objects.get(id=pk)
    comm = TicketComment(memberid=tm, ticketid=ticket, comment=comment)
    comm.save()
    return redirect('ticketSys:detail', pk)


def changeState(request, pk):
    s = request.POST['state']
    t = Ticket.objects.get(id=pk)
    # check if the member able to change the state of the ticket
    # if state was  'waiting_it'
    # the IT members  or All heads only can be able to change the state
    # NOTE any Managerial head begin with X
    #(0, 'WAITING_HR'), (1, 'WAITING_IT'), (2, 'WAITING'), (3, 'SOLVED')
    if t.state == 1:
        print ('plzpzlz')
        # check loged must be IT members or all heads
        member = get_object_or_404(RTMember,pk=request.user) # thats the logged in member in RT table
        if (member.role[0]=='X')or (member.role=='IT') :
            print ('plapla')
            #if t.state is not s:
            # stateChanged(s) #to notify who should be notified by email or whatever
            t.state = s
            t.save()


    return redirect('ticketSys:detail', pk)


class TicketCreate(CreateView):
    model = Ticket
    fields = ['userid', 'state', 'title', 'content']  # member id should be taken from the logged in user

    def form_valid(self, form):
        ticket = form.save(commit=False)
        user = self.request.user
        ticket.memberid = getTicketMember(user)
        return super(TicketCreate, self).form_valid(form)


def dashBoard(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'ticketSys/dashboard.html', context)


def getTicketMember(user):
    rtmember = RTMember.objects.get(userid=user)
    ticketmember = TicketMember.objects.get(memberid=rtmember)
    return ticketmember
