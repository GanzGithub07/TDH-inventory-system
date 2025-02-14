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
    if request.method == 'POST' and form.validate_on_submit():
        item = Item()
        form.populate_obj(item) #populate the item instance with the request form, WTForm automatically populate form with the request form data
        
        
        # Save the new item to the database
        db.session.add(item)
        db.session.commit()
        
        flash("Item added successfully!", "success")
        return redirect(url_for('item.index'))
    elif request.method == 'GET':     
        return render_template('item_index.html', form=form)


@item_bp.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def delete_item(id):
    try:
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        flash(f'{item.name} successfully deleted')
        return '', 200
    
    except Exception as e:
        flash(f'Error: {e}')
        return redirect(url_for('item.index'))
    
    
@item_bp.route('/update/<int:id>', methods=['PUT', 'GET'])
@login_required
def update_item(id):
    if request.method == 'GET':
        item = Item.query.get_or_404(id)
        
        form = ItemForm(obj=item) #fill the item form with the data of queried item
        
        
        print(form.item_id)
        
        return render_template('partials/item_form.html', form=form) 
    
    elif request.method == 'PUT':
        try:
            form = ItemForm()
            item = Item.query.get_or_404(id)
            form.populate_obj(item)
            
            item.modified = True
            db.session.commit()
            
            all_item = Item.query.all()
            return render_template('view_items.html', all_item=all_item)
        except Exception as e:
            flash(e)
            return "", 500
        


@item_bp.route('/view_items', methods=['GET'])
def view_items():
    all_item = Item.query.all()
    return render_template('view_items.html', all_item=all_item)
    