"""
Main entry point for the Smart Band Edge Service Flask application.

This module initializes the Flask app, sets up the database, creates a test device if needed,
and registers the IAM and Health API blueprints.
"""
from flask import Flask

from health.application.routes import health_api
from iam.application.routes import iam_api
from iam.infrastructure.repositories import get_or_create_test_device
from shared.infrastructure.database import init_db

app = Flask(__name__)

# Initialize database
init_db()

# Initialize test device
get_or_create_test_device()

# Register blueprints
app.register_blueprint(iam_api)
app.register_blueprint(health_api)

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="localhost", port=5000, debug=True)
