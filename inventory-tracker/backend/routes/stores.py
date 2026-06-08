from flask import Blueprint
from flask import jsonify
from flask import request

from app import db
from models import Store

stores_bp = Blueprint(
    "stores",
    __name__,
    url_prefix="/stores"
)


@stores_bp.route("/", methods=["GET"])
def get_stores():

    stores = Store.query.all()

    result = []

    for s in stores:
        result.append({
            "id": s.id,
            "store_name": s.store_name,
            "location": s.location
        })

    return jsonify(result)


@stores_bp.route("/", methods=["POST"])
def add_store():

    data = request.json

    store = Store(
        store_name=data["store_name"],
        location=data["location"]
    )

    db.session.add(store)
    db.session.commit()

    return jsonify({
        "message": "Store Added"
    })