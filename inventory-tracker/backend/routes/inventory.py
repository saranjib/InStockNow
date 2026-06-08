from flask import Blueprint
from flask import jsonify
from flask import request

from app import db
from models import Inventory

inventory_bp = Blueprint(
    "inventory",
    __name__,
    url_prefix="/inventory"
)


@inventory_bp.route("/", methods=["GET"])
def get_inventory():

    inventory = Inventory.query.all()

    result = []

    for item in inventory:

        result.append({
            "id": item.id,
            "store_id": item.store_id,
            "product_id": item.product_id,
            "quantity": item.quantity
        })

    return jsonify(result)


@inventory_bp.route("/", methods=["POST"])
def add_inventory():

    data = request.json

    inventory = Inventory(
        store_id=data["store_id"],
        product_id=data["product_id"],
        quantity=data["quantity"]
    )

    db.session.add(inventory)
    db.session.commit()

    return jsonify({
        "message": "Inventory Added"
    })


@inventory_bp.route("/update/<int:id>",
                    methods=["PUT"])
def update_inventory(id):

    inventory = Inventory.query.get(id)

    if not inventory:
        return jsonify({
            "message": "Inventory not found"
        }), 404

    data = request.json

    inventory.quantity = data["quantity"]

    db.session.commit()

    return jsonify({
        "message": "Inventory Updated"
    })