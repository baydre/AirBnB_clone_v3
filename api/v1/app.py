#!/usr/bin/python3

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Register the blueprint app_views to the Flask instance app
# app.register_blueprint(app_views, url_prefix="/api/v1")

# Declare a method to handle teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

if __name__ == "__main__":
    # Set host and port based on environment variables or use default values
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))

    # Run the Flask server with the specified host, port, and threaded=True
    app.run(host=host, port=port, threaded=True)
