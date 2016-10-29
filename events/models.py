from django.db import models
from django.contrib.auth.models import User
from foreignClubs.models import Club, Head


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=1000)
    open = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()
    attendee_num = models.IntegerField()


class Reservation(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="reservation_club")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reservation_event")
    max_num = models.IntegerField()
    current_num = models.IntegerField()


class Role(models.Model):
    name = models.CharField(max_length=1000)


class Organizer(models.Model):
    name = models.CharField(max_length=1000)
    head = models.ForeignKey(Head, on_delete=models.CASCADE, related_name="organizer_head")
    # todo bla bla bla to be added @morsy
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="organize_event")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="organizer_role")


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendee_event")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendee")
