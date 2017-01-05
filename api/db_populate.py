from peewee import *
import datetime
from models import Event

#Event.create(name="Prueba", place = "Granada", date=datetime.datetime.now(),
#                summary = "A simple test").save()

q = Event.select().tuples()
for qq in q:
    print(qq)
