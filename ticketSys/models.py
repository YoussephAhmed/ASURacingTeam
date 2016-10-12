from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from rtMembers.models import RTMember


class TicketMember(models.Model):  # table for RTMembers inrolled in the ticketSystem
    memberid = models.ForeignKey(RTMember, on_delete=models.CASCADE)#TODO Need to be a oneToOne relation
    #  the member from RTMembers

    # def __str__(self): #todo this makes a problem in the Admin panel need a solution
    #     return self.memberid


class Ticket(models.Model):
    memberid = models.ForeignKey(TicketMember, on_delete=models.CASCADE)  # RTmember who issued the ticket
    userid = models.ForeignKey(User, on_delete=models.CASCADE)  # the user who the ticket is about
    state = models.CharField(max_length=1000)  # the current state of the ticket
    title = models.CharField(max_length=1000)  # the title
    content = models.CharField(max_length=1000)  # the content


class TicketComment(models.Model):
    memberid = models.ForeignKey(TicketMember, on_delete=models.CASCADE)
    ticketid = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)


class CommentImg(models.Model):
    commentid = models.ForeignKey(TicketComment, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)


class TicketImg(models.Model):
    ticketid = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
