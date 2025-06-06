from peewee import Model, AutoField, CharField, FloatField, DateTimeField

from shared.infrastructure.database import db


class HealthRecord(Model):
    id = AutoField()
    device_id = CharField()
    bpm = FloatField()
    created_at = DateTimeField()

    class Meta:
        database = db
        table_name = 'health_records'
