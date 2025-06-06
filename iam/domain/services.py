from typing import Optional

from iam.domain.entities import Device


class AuthService:
    def __init__(self):
        """Initialize the AuthService."""
        pass

    @staticmethod
    def authenticate(device: Optional[Device]) -> bool:
        """Authenticate a device using its ID and API key.
        Args:
            device (Optional[Device]): The device to authenticate.
        Returns:
            bool: True if the device is authenticated, False otherwise.
        """
        return device is not None