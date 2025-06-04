"""
Peewee ORM model for devices.

Defines the Device database table structure for storing registered device information.
"""
from peewee import Model, CharField, DateTimeField

from shared.infrastructure.database import db


class Device(Model):
    """
    ORM model for the devices table.
    Represents a registered device entry in the database.
    """
    device_id = CharField(primary_key=True)
    api_key = CharField()
    created_at = DateTimeField()

    class Meta:
        database = db
        table_name = 'devices'

