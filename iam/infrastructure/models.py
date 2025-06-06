"""Peewee models for the IAM bounded context."""
from peewee import CharField, DateTimeField, Model
from shared.infrastructure.database import db


class Device(Model):
    """Peewee model for the Device entity in the IAM bounded context."""
    device_id   = CharField(primary_key=True)
    api_key     = CharField(unique=True, null=False)
    created_at  = DateTimeField()

    class Meta:
        """Metadata class for the Device model."""
        database = db
        table_name = 'devices'