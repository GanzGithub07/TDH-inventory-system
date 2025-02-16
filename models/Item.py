from extensions import db


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    category = db.Column(db.String)
    purchase_price = db.Column(db.Float)
    selling_price = db.Column(db.Float)
    purchase_date = db.Column(db.DateTime)
    description = db.Column(db.String)
    batch_no = db.Column(db.String)
    supplier = db.Column(db.String)
    total_price = db.Column(db.Float)
    expiration_date = db.Column(db.DateTime)