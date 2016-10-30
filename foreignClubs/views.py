from django.shortcuts import render, get_object_or_404, redirect
from foreignClubs.models import Club, Head
from django.contrib.auth.models import User
from django.db.models import Q


# **** Head Backend Task ****
# Add a new Head to the head table associated with a Club, and view current heads and their clubs.
# Accessed from Admin Panel
# In Club app.

# The view should send all the current heads(names, club names)
# it Shall receive the info for a new Head and add it to the DataBase
# The info needed for a new head is User and Club
# So it should send all the clubs and users

def heads(request):
    if request.method == "GET":  # Opening the page for the first time to display the head list
        heads = Head.objects.all()
        clubs = Club.objects.all()
        users = User.objects.filter(
            Q(rtMember__isnull=True) & Q(
                heads__isnull=True))  # to prevent showing users that are RTMembers or already heads
        context = {'heads': heads, 'clubs': clubs, 'users': users}
        return render(request, "foreignClubs/heads.html", context)
    else:  # adding a new head
        user = User.objects.get(id=request.POST['userid'])
        club = Club.objects.get(id=request.POST['clubid'])
        try:
            head = Head(user=user, club=club)
            head.save()
        except:
            return render(request, "foreignClubs/one_head.html", {'head': "ERROR can't save"})
        return render(request, "foreignClubs/one_head.html", {'head': head})
