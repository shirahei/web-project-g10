from flask import Blueprint, render_template,request
from utilities.db.items import Items

# catalog blueprint definition
search = Blueprint('search', __name__, static_folder='static', static_url_path='/search', template_folder='templates')


# Routes
@search.route('/search')
def index():
    return render_template('search.html')


@search.route('/search',methods=["POST"])
def searchItems():
    category = request.form.get('category')
    condition = request.form.get('condition')
    items = Items.search_item(category,condition)
    return render_template('search.html',items_list=items)


