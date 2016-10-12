from idlelib.tabbedpages import TabbedPageSet

from django.shortcuts import render, get_object_or_404
from .models import Ticket
from django.views import generic


def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {'ticket': ticket}
    return render(request, 'ticketSys/detail.html', context)


# def add(request):

def dashBoard(request):
    tickets = Ticket.objects.all();
    context = {'tickets': tickets}
    return render(request, 'ticketSys/dashboard.html', context)
