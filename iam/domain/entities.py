"""
Domain entity for devices.

Represents a device registered in the IAM system.
"""
class Device:
    def __init__(self, device_id, api_key, created_at):
        self.device_id = device_id
        self.api_key = api_key
        self.created_at = created_at