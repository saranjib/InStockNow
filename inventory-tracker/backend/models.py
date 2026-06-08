from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120),
                      unique=True,
                      nullable=False)

    password = db.Column(db.String(255),
                         nullable=False)

    role = db.Column(db.String(20),
                     default="customer")


class Store(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer,
                   primary_key=True)

    store_name = db.Column(db.String(150),
                           nullable=False)

    location = db.Column(db.String(255),
                         nullable=False)


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer,
                   primary_key=True)

    product_name = db.Column(db.String(150),
                             nullable=False)

    description = db.Column(db.Text)


class Inventory(db.Model):

    __tablename__ = "inventory"

    id = db.Column(db.Integer,
                   primary_key=True)

    store_id = db.Column(
        db.Integer,
        db.ForeignKey("stores.id")
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id")
    )

    quantity = db.Column(db.Integer,
                         default=0)


class Reservation(db.Model):

    __tablename__ = "reservations"

    id = db.Column(db.Integer,
                   primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    store_id = db.Column(
        db.Integer,
        db.ForeignKey("stores.id")
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id")
    )

    quantity = db.Column(db.Integer)

    reserved_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )