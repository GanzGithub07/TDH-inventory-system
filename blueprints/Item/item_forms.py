from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length


class ItemForm(FlaskForm):
    item_id = IntegerField('item_id', validators=[DataRequired()])
    name = StringField()
    quantity = IntegerField()
    category = StringField()
    purchase_price = FloatField()
    selling_price = FloatField()
    purchase_date = DateField()
    description = StringField()
    batch_no = StringField()
    supplier = StringField()
    total_price = FloatField()
    expiration_date = DateField()
    submit = SubmitField('Add Item')