#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> jsonify:
    """
    Handles GET requests to the root endpoint.
    
    Returns:
        A JSON response with the message "Bienvenue".
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

