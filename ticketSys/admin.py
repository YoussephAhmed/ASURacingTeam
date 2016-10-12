from django.contrib import admin
from .models import TicketMember,Ticket,TicketComment,CommentImg,TicketImg

admin.site.register(TicketMember)
admin.site.register(Ticket)
admin.site.register(TicketComment)
admin.site.register(CommentImg)
admin.site.register(TicketImg)
