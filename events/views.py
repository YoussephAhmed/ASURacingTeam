from django.shortcuts import render, get_object_or_404, redirect
from foreignClubs.models import Club, Head
from events.models import Event, Role, Organizer
from django.contrib.auth.models import User
from django.db.models import Q


# **** Organizer Backend Task ****
# Add a new organizer to the Organizer table, and view current organizers.
# Accessed from Admin Panel.
# In Event app.

# The view should send all the current organizers associated with the current club
# which is obtained from the head logged in
# It Shall also receives the info for a new Organizer and add it to the DataBase
# The info needed for a new Organizer is name and Head and Event and Role
# So it should send all the events and roles and fetch the head from the logged in user

def organizers(request):
    if request.method == "GET":  # Opening the page for the first time to display the head list
        events = Event.objects.filter(open=True)  # only show currently open events
        # events = Event.objects.filter()  # test
        roles = Role.objects.all()
        organizers = Organizer.objects.all()
        context = {'events': events, 'roles': roles, 'organizers': organizers}
        return render(request, "events/organizers.html", context)
    else:  # adding a new head
        name = request.POST['name']
        event = Event.objects.get(id=request.POST['eventid'])
        role = Role.objects.get(id=request.POST['roleid'])
        try:
            head = Head.objects.get(user=request.user)
        except:
            return render(request, "events/one_organizer.html", {'organizer': "ERROR no head"})
        try:
            organizer = Organizer(event=event, name=name, role=role, head=head)
            organizer.save()
        except:
            return render(request, "events/one_organizer.html", {'organizer': "ERROR can't save"})
        return render(request, "events/one_organizer.html", {'organizer': organizer})
