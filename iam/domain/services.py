"""
Authentication service for device IAM.

Provides business logic for authenticating devices using device_id and API key.
"""
from ..infrastructure.repositories import DeviceRepository

class AuthService:
    """
    Service for authenticating devices.
    """
    def __init__(self, device_repository: DeviceRepository):
        """
        Initialize the AuthService with a device repository.
        """
        self.device_repository = device_repository

    def authenticate(self, device_id: str, api_key: str) -> bool:
        """
        Authenticate a device by its ID and API key.
        Args:
            device_id (str): The device identifier.
            Api_key (str): The API key for the device.
        Returns:
            bool: True if authentication is successful, False otherwise.
            :param device_id:
            :param api_key:
        """
        device = self.device_repository.find_by_id_and_api_key(device_id, api_key)
        return device is not None

