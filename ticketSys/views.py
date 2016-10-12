from django.shortcuts import render, get_object_or_404
from .models import Ticket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView


def detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    context = {'ticket': ticket}
    return render(request, 'ticketSys/detail.html', context)


class TicketCreate(CreateView):
    model = Ticket
    fields = ['memberid','userid', 'state', 'title', 'content']#member id should be taken from the logged in user


def dashBoard(request):
    tickets = Ticket.objects.all();
    context = {'tickets': tickets}
    return render(request, 'ticketSys/dashboard.html', context)
