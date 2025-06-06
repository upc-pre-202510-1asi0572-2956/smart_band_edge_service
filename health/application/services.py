from health.domain.entities import HealthRecord
from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository
from iam.infrastructure.repositories import DeviceRepository


class HealthRecordApplicationService:
    def __init__(self):
        self.health_record_repository = HealthRecordRepository()
        self.health_record_service = HealthRecordService()
        self.device_repository = DeviceRepository()

    def create_health_record(self, device_id: str, bpm: float, created_at: str, api_key: str) -> HealthRecord:
        if not self.device_repository.find_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found or API key is invalid")
        record = self.health_record_service.create_record(device_id, bpm, created_at)
        return self.health_record_repository.save(record)