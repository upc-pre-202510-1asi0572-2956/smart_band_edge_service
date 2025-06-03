from flask import Blueprint, request, jsonify
from ..domain.services import HealthRecordService
from ..infrastructure.repositories import HealthRecordRepository
from ...iam.application.routes import authenticate_request
from ...iam.infrastructure.repositories import DeviceRepository

health_api = Blueprint("health_api", __name__)

# Initialize dependencies
health_record_service = HealthRecordService(HealthRecordRepository())
device_repository = DeviceRepository()

@health_api.route("/api/v1/health-monitoring/data-records", methods=["POST"])
def create_health_record():
    auth_result = authenticate_request()
    if auth_result:
        return auth_result

    data = request.json
    try:
        device_id = data["deviceId"]
        # Validate device_id exists in IAM context
        if not device_repository.find_by_id_and_api_key(device_id, request.headers.get("X-API-Key")):
            return jsonify({"error": "Device not found"}), 404
        bpm = data["bpm"]
        timestamp = data.get("timestamp", "unknown")
        record = health_record_service.create_record(device_id, bpm, timestamp)
        return jsonify({
            "id": record.id,
            "deviceId": record.device_id,
            "bpm": record.bpm,
            "timestamp": record.timestamp
        }), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400