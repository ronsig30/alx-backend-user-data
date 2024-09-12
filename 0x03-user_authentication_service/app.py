#!/usr/bin/env python3

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home() -> jsonify:
    """
    Handles GET requests to the root endpoint.

    Returns:
        A JSON response with the message "Bienvenue".
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> jsonify:
    """
    Handles POST requests to register a new user.

    Expects form data with 'email' and 'password'.

    Returns:
        A JSON response indicating the result of the registration attempt.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
