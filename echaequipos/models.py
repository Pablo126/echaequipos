from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Player(models.Model):
    user = models.ForeignKey('auth.User')
    age = models.IntegerField()
    position = models.IntegerField()
    rate = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def createPlayer(self):
        self.save()
