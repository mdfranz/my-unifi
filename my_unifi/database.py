from peewee import SqliteDatabase, Model, CharField, TextField, DateTimeField, BooleanField, ForeignKeyField 
from datetime import datetime

db = SqliteDatabase('database.sqlite3')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Guest(BaseModel):
    name = CharField(unique=True)
    admin = BooleanField(default=False)
    notes = TextField()

class Host(BaseModel):
    alias = CharField()
    name = CharField(unique=True)
    mac_addr = CharField(unique=True)
    first_seen = DateTimeField(default=datetime.now)
    owner = ForeignKeyField(Guest, backref='hosts')
    notes = TextField()

for m in [Host, Guest]:
    if not m.table_exists():
        print("Creating {} database table...".format(m.__qualname__))
        m.create_table()

