from peewee import *
import peeweedbevolve

db = PostgresqlDatabase('test_OC')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    """
        This models represents Users in database
    """
    username = CharField(unique=True)
    password = CharField()
    email = CharField(default="")
    join_date = DateTimeField()
    is_admin = BooleanField(default=False)

class Event(BaseModel):
    """
        This models represents each event created by a Community
    """
    name = CharField()
    place = CharField()
    date = DateTimeField()
    summary = TextField()
    going = ForeignKeyField(User, related_name='members_going', null = True)
    not_going = ForeignKeyField(User, related_name='members__not_going', null = True)

class Community(BaseModel):
    pk = IntegerField()
    name = CharField()
    location = CharField()
    users = ForeignKeyField(User, related_name='members')
    events = ForeignKeyField(Event, related_name='events')



db.evolve()
