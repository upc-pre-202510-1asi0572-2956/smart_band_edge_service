from .models import HealthRecord as HealthRecordModel
from ..domain.entities import HealthRecord


class HealthRecordRepository:
    def save(self, health_record):
        record = HealthRecordModel.create(
            device_id=health_record.device_id,
            bpm=health_record.bpm,
            timestamp=health_record.timestamp
        )
        return HealthRecord(
            health_record.device_id,
            health_record.bpm,
            health_record.timestamp,
            record.id
        )