from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class RTMember(models.Model):  # For  holding all RT members and assinging a role
    role = models.CharField(max_length=1000)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.userid.username + ' - '+ self.role