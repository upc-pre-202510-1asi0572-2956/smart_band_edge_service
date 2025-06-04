"""
Domain service for health record operations.

Provides business logic for creating and validating health records.
"""
from datetime import datetime

from dateutil.parser import parse

from health.domain.entities import HealthRecord

class HealthRecordService:
    """
    Service for managing health records.
    """
    def __init__(self, health_record_repository):
        """
        Initialize the service with a health record repository.
        """
        self.health_record_repository = health_record_repository

    def create_record(self, device_id, bpm, created_at):
        """
        Create and validate a health record, then save it.
        Args:
            device_id (str): The device identifier.
            bpm (float): Beats per minute.
            created_at (str): ISO8601 timestamp or 'unknown'.
        Returns:
            HealthRecord: The created health record entity.
        Raises:
            ValueError: If data is invalid.
        """
        print(f"Creating health record for device {device_id} with BPM {bpm} at {created_at}")
        try:
            bpm = float(bpm)
            if not (0 <= bpm <= 200):
                raise ValueError("Invalid BPM value")
            parsed_created_at = parse(created_at) if created_at != "unknown" else datetime.today()
            print(f"Creating health record for device {device_id} with BPM {bpm} at {created_at}")
            created_at_str = parsed_created_at.isoformat()
            print(f"Parsed created_at: {created_at_str}")
        except (ValueError, TypeError):
            raise ValueError("Invalid data format")

        record = HealthRecord(device_id, bpm, created_at_str)
        return self.health_record_repository.save(record)

