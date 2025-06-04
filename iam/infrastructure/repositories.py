"""
Repository and utility functions for device persistence and lookup.

Handles device creation, lookup, and test device initialization using Peewee ORM models.
"""
from typing import Optional

from iam.infrastructure.models import Device as DeviceModel
from iam.domain.entities import Device


def get_or_create_test_device() -> Optional[Device]:
    """
    Get or create a test device in the database.
    Returns:
        Device or None: The test device entity.
    """
    from datetime import datetime
    device, created = DeviceModel.get_or_create(
        device_id="smart-band-001",
        defaults={
            'api_key': "test-api-key-123",
            'created_at': datetime.utcnow()
        }
    )
    return Device(device.device_id, device.api_key, device.created_at)


class DeviceRepository:
    """
    Repository for managing Device persistence and lookup.
    """
    def find_by_id_and_api_key(self, device_id: str, api_key: str) -> Optional[Device]:
        """
        Find a device by its ID and API key.
        Args:
            device_id (str): The device identifier.
            api_key (str): The API key for the device.
        Returns:
            Device or None: The found device entity or None if not found.
        """
        try:
            device = DeviceModel.get(
                (DeviceModel.device_id == device_id) &
                (DeviceModel.api_key == api_key)
            )
            return Device(device.device_id, device.api_key, device.created_at)
        except DeviceModel.get().DoesNotExist:
            return None

