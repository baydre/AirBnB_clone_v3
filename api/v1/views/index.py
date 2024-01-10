#!/usr/bin/python3

# api/v1/views/index.py
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns a JSON response with the status."""
    return jsonify({"status": "OK"})
