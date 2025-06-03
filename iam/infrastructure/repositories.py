from typing import Optional
from ..domain.entities import Device
from .models import Device as DeviceModel

class DeviceRepository:
    def find_by_id_and_api_key(self, device_id: str, api_key: str) -> Optional[Device]:
        try:
            device = DeviceModel.get(
                (DeviceModel.device_id == device_id) &
                (DeviceModel.api_key == api_key)
            )
            return Device(device.device_id, device.api_key, device.created_at)
        except DeviceModel.DoesNotExist:
            return None

    def get_or_create_test_device(self):
        from datetime import datetime
        device, created = DeviceModel.get_or_create(
            device_id="smart-band-001",
            defaults={
                'api_key': "test-api-key-123",
                'created_at': datetime.utcnow()
            }
        )
        return Device(device.device_id, device.api_key, device.created_at)