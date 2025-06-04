"""
Flask routes for device authentication and IAM endpoints.

This module defines the API endpoints for device authentication and related IAM operations.
"""
from flask import Blueprint, request, jsonify

from iam.domain.services import AuthService
from iam.infrastructure.repositories import DeviceRepository

iam_api = Blueprint("iam_api", __name__)

# Initialize dependencies
auth_service = AuthService(DeviceRepository())

def authenticate_request():
    """
    Authenticate a request using device_id and X-API-Key from headers.
    Returns a Flask response with error if authentication fails, otherwise None.
    """
    device_id = request.json.get("device_id") if request.json else None
    api_key = request.headers.get("X-API-Key")
    if not device_id or not api_key:
        return jsonify({"error": "Missing device_id or X-API-Key"}), 401
    if not auth_service.authenticate(device_id, api_key):
        return jsonify({"error": "Invalid device_id or API key"}), 401
    return None

