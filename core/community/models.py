from django.db import models
from users.models import CustomUser
# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=254)
    place = models.CharField(max_length=255)
    date = models.DateTimeField()
    going = models.ForeignKey(CustomUser,related_name="assistants")
    notGoing = models.ForeignKey(CustomUser,related_name="avoiding")

    def __str__(self):
        return self.name



class Community(models.Model):

    name = models.CharField(max_length=254)
    city = models.CharField(max_length = 212)
    description = models.TextField()
    admins = models.ManyToManyField(CustomUser,related_name="admins")
    events = models.ManyToManyField(Event,related_name="events", blank = True)

    def __str__(self):
        return self.name
