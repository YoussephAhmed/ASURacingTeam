
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=1000)


class Head(models.Model):
    # todo Check this must be one to one
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="heads")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="club_heads")
