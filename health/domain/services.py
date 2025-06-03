from datetime import datetime

from dateutil.parser import parse

from .entities import HealthRecord


class HealthRecordService:
    def __init__(self, health_record_repository):
        self.health_record_repository = health_record_repository

    def create_record(self, device_id, bpm, timestamp):
        try:
            bpm = float(bpm)
            if not (0 <= bpm <= 200):
                raise ValueError("Invalid BPM value")
            parsed_timestamp = parse(timestamp) if timestamp != "unknown" else datetime.utcnow()
            timestamp_str = parsed_timestamp.isoformat()
        except (ValueError, TypeError):
            raise ValueError("Invalid data format")

        record = HealthRecord(device_id, bpm, timestamp_str)
        return self.health_record_repository.save(record)