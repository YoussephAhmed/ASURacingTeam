from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rtMembers.models import RTMember
from ticketSys.models import TicketMember, TicketComment, Ticket
from django.contrib.auth.models import User


def detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    comms = TicketComment.objects.filter(ticketid_id=pk)
    context = {'ticket': ticket, 'comments': comms}
    return render(request, 'ticketSys/detail.html', context)


def addComment(request, pk):
    comment = request.POST['comment']
    user = request.user
    tm = getTicketMember(user)
    ticket = Ticket.objects.get(id=pk)
    comm = TicketComment(memberid=tm, ticketid=ticket, comment=comment)
    comm.save()
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
