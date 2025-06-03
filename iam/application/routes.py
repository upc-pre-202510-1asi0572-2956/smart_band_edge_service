from flask import Blueprint, request, jsonify

from ..domain.services import AuthService
from ..infrastructure.repositories import DeviceRepository

iam_api = Blueprint("iam_api", __name__)

# Initialize dependencies
auth_service = AuthService(DeviceRepository())

def authenticate_request():
    device_id = request.json.get("deviceId") if request.json else None
    api_key = request.headers.get("X-API-Key")
    if not device_id or not api_key:
        return jsonify({"error": "Missing deviceId or X-API-Key"}), 401
    if not auth_service.authenticate(device_id, api_key):
        return jsonify({"error": "Invalid deviceId or API key"}), 401
    return None