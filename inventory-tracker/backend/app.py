from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:password@localhost/inventorydb'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    from routes.auth import auth_bp
    from routes.products import products_bp
    from routes.stores import stores_bp
    from routes.inventory import inventory_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(stores_bp)
    app.register_blueprint(inventory_bp)

    @app.route("/")
    def home():
        return {
            "message": "ShelfSync API Running"
        }

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)