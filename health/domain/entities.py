import datetime


class HealthRecord:
    def __init__(self, device_id: str, bpm: float, created_at: datetime, id: int = None):
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.created_at = created_at