from flask import Flask
from iam.application.routes import iam_api
from health.application.routes import health_api
from shared.infrastructure.database import init_db
from iam.infrastructure.repositories import DeviceRepository

app = Flask(__name__)

# Initialize database
init_db()

# Initialize test device
DeviceRepository().get_or_create_test_device()

# Register blueprints
app.register_blueprint(iam_api)
app.register_blueprint(health_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)