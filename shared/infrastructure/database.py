from peewee import SqliteDatabase

# Initialize SQLite database
db = SqliteDatabase('smart_band.db')

def init_db():
    db.connect()
    from ...iam.infrastructure.models import Device
    from ...health.infrastructure.models import HealthRecord
    db.create_tables([Device, HealthRecord], safe=True)
    db.close()