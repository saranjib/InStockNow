from flask import Blueprint
from flask import jsonify
from flask import request

from app import db
from models import Product
from models import Inventory

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/", methods=["GET"])
def get_products():

    products = Product.query.all()

    result = []

    for p in products:

        result.append({
            "id": p.id,
            "name": p.product_name,
            "description": p.description
        })

    return jsonify(result)


@products_bp.route("/", methods=["POST"])
def add_product():

    data = request.json

    product = Product(
        product_name=data["product_name"],
        description=data["description"]
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product added"
    })


@products_bp.route("/search/<name>")
def search_product(name):

    products = Product.query.filter(
        Product.product_name.ilike(
            f"%{name}%"
        )
    ).all()

    result = []

    for p in products:

        stock = Inventory.query.filter_by(
            product_id=p.id
        ).all()

        result.append({
            "product": p.product_name,
            "stock": [
                {
                    "store_id": s.store_id,
                    "quantity": s.quantity
                }
                for s in stock
            ]
        })

    return jsonify(result)