from django.shortcuts import render, get_object_or_404
from .models import Ticket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rtMembers.models import RTMember
from ticketSys.models import TicketMember
from django.contrib.auth.models import User


def detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    context = {'ticket': ticket}
    return render(request, 'ticketSys/detail.html', context)


class TicketCreate(CreateView):
    model = Ticket
    fields = ['userid', 'state', 'title', 'content']  # member id should be taken from the logged in user

    def form_valid(self, form):
        ticket = form.save(commit=False)
        user = self.request.user
        rt = RTMember.objects.get(userid=user)
        tm = TicketMember.objects.get(memberid=rt)
        ticket.memberid = tm
        return super(TicketCreate, self).form_valid(form)


def dashBoard(request):
    tickets = Ticket.objects.all();
    context = {'tickets': tickets}
    return render(request, 'ticketSys/dashboard.html', context)
