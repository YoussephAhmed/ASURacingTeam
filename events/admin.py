from django.contrib import admin
from .models import Event,Reservation,Role,Organizer,Attendee

admin.site.register(Event)
admin.site.register(Reservation)
admin.site.register(Role)
admin.site.register(Organizer)
admin.site.register(Attendee)
