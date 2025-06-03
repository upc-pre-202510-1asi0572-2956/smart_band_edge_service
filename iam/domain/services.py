from ..infrastructure.repositories import DeviceRepository

class AuthService:
    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    def authenticate(self, device_id: str, api_key: str) -> bool:
        device = self.device_repository.find_by_id_and_api_key(device_id, api_key)
        return device is not None
