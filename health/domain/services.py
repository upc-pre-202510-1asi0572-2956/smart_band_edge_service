from datetime import timezone, datetime

from dateutil.parser import parse

from health.domain.entities import HealthRecord


class HealthRecordService:
    def __init__(self):
        pass

    @staticmethod
    def create_record(device_id: str, bpm: float, created_at: str | None) -> HealthRecord:
        try:
            bpm = float(bpm)
            if not (0 <= bpm <= 200):
                raise ValueError("BPM must be between 0 and 200")
            if created_at:
                parsed_created_at = parse(created_at).astimezone(timezone.utc)
            else:
                parsed_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid BPM or created_at format")

        return HealthRecord(device_id, bpm, parsed_created_at)