# Each model is represented by a class that subclasses django.db.models.Model.
# Each model has a number of class variables,
# each of which represents a database field in the model.

from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# For  holding all roles

class Roles:
    ROLES = (
        (0, 'IT'), (1, 'XIT'), (2, 'REC'), (3, 'XREC'), (4, 'OD'), (5, 'XOD'), (6, 'MARK'), (7, 'XMARK'), (8, 'OTHER'),
        (9, 'XOTHER')
    )


# Each field is represented by an instance of a Field class
# CharField for character fields

# Relationship is defined, using ForeignKey. that tells django for example each
# RTMenmber instance created from this class will be related to a single role.


# For  holding all RT members and assinging a role

class RTMember(models.Model):
    role = models.IntegerField(choices=Roles.ROLES)
    #  must be a one to one relationship
    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(to=User, related_name='rtMember')

    # to return data as a string
    def __str__(self):

        return self.user.username + ' - ' + Roles.ROLES[self.role][1]
