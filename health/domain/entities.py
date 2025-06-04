"""
Domain entity for health records.

Represents a health record associated with a device.
"""
class HealthRecord:
    """
    HealthRecord entity representing a health data record.
    """
    def __init__(self, device_id, bpm, created_at, id=None):
        """
        Initialize a HealthRecord entity.
        Args:
            device_id (str): The device identifier.
            bpm (float): Beats per minute.
            created_at (str): ISO8601 timestamp.
            id (int, optional): Record ID.
        """
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.created_at = created_at

