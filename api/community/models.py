from django.db import models

# Create your models here.

class Community(models.Model):

    name = models.CharField(max_lenght=254)
    city = models.CharField(max_lenght = 212)
    summary = models.TextField()
    admins = models.ForeignKey(User)
