from flask import Blueprint
from flask import request
from flask import jsonify

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app import db
from models import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    existing = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing:
        return jsonify({
            "message": "Email already exists"
        }), 400

    user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(
            data["password"]
        )
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Registration successful"
    })


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(
        email=data["email"]
    ).first()

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    if not check_password_hash(
            user.password,
            data["password"]):

        return jsonify({
            "message": "Invalid password"
        }), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    })