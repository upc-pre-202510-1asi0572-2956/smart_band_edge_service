"""Domain entities for the IAM module."""
class Device:
    """Represents a device in the IAM system.

    Attributes:
        device_id (str): Unique identifier for the device.
        api_key (str): API key associated with the device.
        created_at (datetime): Timestamp when the device was created.
    """


    def __init__(self, device_id:str, api_key: str, created_at):
        """Initialize a Device instance.
        Args:
            device_id (str): Unique identifier for the device.
            api_key (str): API key associated with the device.
            created_at (datetime): Timestamp when the device was created.
        """
        self.device_id = device_id
        self.api_key = api_key
        self.created_at = created_at