from django.db import models
import random
import string
import datetime
# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey('users.CustomUser')
    text = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    replies = models.ManyToManyField("self")

    def __str__(self):
        return self.author.user.username

class Event(models.Model):

    name = models.CharField(max_length=254)
    place = models.CharField(max_length=255)
    date = models.DateTimeField()
    going = models.ManyToManyField('users.CustomUser',related_name="assistants")
    notGoing = models.ManyToManyField('users.CustomUser',related_name="avoiding", blank=True)
    slug = models.SlugField(primary_key=True, unique=True, editable=True, blank=True)
    comments = models.ManyToManyField(Comment, blank=True, null=True)

    def save(self, *args, **kwargs):
        while not self.slug:
            ret = []
            ret.extend(random.sample(string.ascii_letters, 2))
            ret.extend(random.sample(string.digits, 2))
            ret.extend(random.sample(string.ascii_letters, 2))

            newslug = ''.join(ret)
            if Event.objects.filter(slug=newslug).count() == 0:
                self.slug = newslug

        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Community(models.Model):

    name = models.CharField(max_length=254)
    city = models.CharField(max_length = 212)
    description = models.TextField()
    admins = models.ManyToManyField('users.CustomUser',related_name="admins")
    events = models.ManyToManyField(Event,related_name="events", blank = True)

    def __str__(self):
        return self.name
