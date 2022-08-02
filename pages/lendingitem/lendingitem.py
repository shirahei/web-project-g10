from flask import Blueprint, render_template,request,session,redirect
from werkzeug.utils import secure_filename
from utilities.db.items import Items
import os
from app import app
uploads_dir = os.path.join('static/media', 'uploads')
os.makedirs(uploads_dir,exist_ok=True)

# catalog blueprint definition
lendingitem = Blueprint('lendingitem', __name__, static_folder='static', static_url_path='/lendingitem', template_folder='templates')


# Routes
@lendingitem.route('/lendingitem')
def index():
    return render_template('lendingitem.html')

@lendingitem.route('/uploadItem',methods=['POST'])
def uploadItem():
    f = request.files['item_image']
    f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
    owner_id = session.get('customer_id')
    category = request.form.get('item_category')
    title = request.form.get('title')
    description = request.form.get('item_description')
    condition = request.form.get('item_condition')
    Items.insert_item(owner_id,title,category,condition,description,f.filename)
    return redirect('/myitems')

