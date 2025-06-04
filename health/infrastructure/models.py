"""
Peewee ORM model for health records.

Defines the HealthRecord database table structure for storing health monitoring data.
"""
from peewee import Model, AutoField, FloatField, CharField

from shared.infrastructure.database import db


class HealthRecord(Model):
    """
    ORM model for the health_records table.
    Represents a health record entry in the database.
    """
    id = AutoField()
    device_id = CharField()
    bpm = FloatField()
    created_at = CharField()

    class Meta:
        database = db
        table_name = 'health_records'

