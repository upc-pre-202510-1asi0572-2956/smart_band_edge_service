from health.domain.entities import HealthRecord
from health.infrastructure.models import HealthRecord as HealthRecordModel

class HealthRecordRepository:

    @staticmethod
    def save(health_record) -> HealthRecord:
        record = HealthRecordModel.create(
            device_id   = health_record.device_id,
            bpm         = health_record.bpm,
            created_at  = health_record.created_at
        )
        return HealthRecord(
            health_record.device_id,
            health_record.bpm,
            health_record.created_at,
            record.id
        )