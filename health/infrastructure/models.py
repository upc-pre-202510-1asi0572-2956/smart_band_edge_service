from peewee import Model, AutoField, FloatField, CharField
from shared.infrastructure.database import db

class HealthRecord(Model):
    id = AutoField()
    device_id = CharField()
    bpm = FloatField()
    timestamp = CharField()

    class Meta:
        database = db