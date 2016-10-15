from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Roles:
    ROLES = (
        (0, 'IT'),(1, 'XIT'), (2, 'REC'),(3, 'XREC'), (4, 'OD'),(5, 'XOD'), (6, 'MARK'), (7, 'XMARK'), (8, 'OTHER'), (9, 'XOTHER')
    )
class RTMember(models.Model):  # For  holding all RT members and assinging a role
    role = models.IntegerField(choices=Roles.ROLES)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.userid.username + ' - '+ str(self.role)
