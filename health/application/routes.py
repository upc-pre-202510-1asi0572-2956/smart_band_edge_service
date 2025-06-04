"""
Flask routes for health monitoring endpoints.

This module defines the API endpoints for creating health records and handles authentication and device validation.
"""
from flask import Blueprint, request, jsonify

from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository
from iam.application.routes import authenticate_request
from iam.infrastructure.repositories import DeviceRepository

health_api = Blueprint("health_api", __name__)

# Initialize dependencies
health_record_service = HealthRecordService(HealthRecordRepository())
device_repository = DeviceRepository()

@health_api.route("/api/v1/health-monitoring/data-records", methods=["POST"])
def create_health_record():
    """
    Create a new health record for a device.
    Expects JSON with 'device_id', 'bpm', and optional 'created_at'.
    Requires valid device authentication.
    """
    print("Starting to create health record")
    auth_result = authenticate_request()
    if auth_result:
        return auth_result

    data = request.json
    try:
        device_id = data["device_id"]
        api_key = request.headers.get("X-API-Key")
        # Validate device_id exists in IAM context
        if not device_repository.find_by_id_and_api_key(device_id, api_key):
            return jsonify({"error": "Device not found"}), 404
        bpm = data["bpm"]
        created_at = data.get("created_at", "unknown")
        # Log creation attempt for debugging
        print(f"Creating health record for device {device_id} with BPM {bpm} at {created_at}")
        record = health_record_service.create_record(device_id, bpm, created_at)
        return jsonify({
            "id": record.id,
            "deviceId": record.device_id,
            "bpm": record.bpm,
            "created_at": record.created_at
        }), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
