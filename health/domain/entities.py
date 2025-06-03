class HealthRecord:
    def __init__(self, device_id, bpm, timestamp, id=None):
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.timestamp = timestamp