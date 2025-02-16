from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from app import db  # Assuming you have set up SQLAlchemy in your app
from blueprints.Item.item_forms import ItemForm  # Import the form
from models.Item import Item  # Import the Item model
# If `auth_form.py` is in the `blueprints` folder



item_bp = Blueprint("item", __name__, template_folder='item_templates', static_folder='item_static')

@item_bp.route('/')
@login_required
def index():
    form = ItemForm()
    return render_template('item_index.html', form=form  )


@item_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        # Create an Item object and populate it with form data
        new_item = Item(
            item_id=form.item_id.data,
            name=form.name.data,
            quantity=form.quantity.data,
            category=form.category.data,
            purchase_price=form.purchase_price.data,
            selling_price=form.selling_price.data,
            purchase_date=form.purchase_date.data,
            description=form.description.data,
            batch_no=form.batch_no.data,
            supplier=form.supplier.data,
            total_price=form.total_price.data,
            expiration_date=form.expiration_date.data
        )
        
        # Save the new item to the database
        db.session.add(new_item)
        db.session.commit()
        
        flash("Item added successfully!", "success")
        return redirect(url_for('item.index'))
    
    return render_template('item_index.html', form=form)



@item_bp.route('/view_items', methods=['GET'])
def view_items():
    categories = ["ALL", "EQUIPMENTS", "DEXTROSE", "MEDICAL SUPPLY", "MEDICINES", "OFFICE SUPPLY", "UTILITY", "LABORATORY"]

    # Get the search and filter parameters
    search_query = request.args.get('search', '').strip()
    selected_category = request.args.get('category', 'ALL')

    # Start with a base query
    query = Item.query

    # Apply search filter
    if search_query:
        query = query.filter(Item.name.ilike(f"%{search_query}%"))

    # Apply category filter (excluding "ALL")
    if selected_category and selected_category != "ALL":
        query = query.filter_by(category=selected_category)

    # Fetch filtered items
    all_items = query.all()

    return render_template('view_items.html', all_item=all_items, categories=categories, selected_category=selected_category)
    #return render_template('view_items.html', all_item=all_item)
    