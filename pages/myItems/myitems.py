from flask import Blueprint, render_template,redirect,session,request
from utilities.db.items import Items

# catalog blueprint definition
myitems = Blueprint('myitems', __name__, static_folder='static', static_url_path='/myItems', template_folder='templates')


# Routes
@myitems.route('/myitems')
def index():
    ownerID = session.get('customer_id')
    myItemsList = Items.get_my_items(ownerID)
    return render_template('myitems.html',itemsList = myItemsList)

@myitems.route('/removeItem/<itemID>')
def removeItem(itemID):
    ownerID = session.get('customer_id')
    Items.remove_item(itemID,ownerID)
    return redirect('/myitems')

@myitems.route('/editItem/<itemID>')
def editItem(itemID):
    ownerID = session.get('customer_id')
    itemForEdit = Items.get_item_by_id(itemID,ownerID)[0]
    return render_template('editItem.html',item=itemForEdit)

@myitems.route('/editItem/<itemID>',methods=['POST'])
def editItemSet(itemID):

    category = request.form.get('category')
    condition = request.form.get('condition')
    description = request.form.get('description')
    title = request.form.get('title')
    Items.edit_item(itemID,category,condition,description,title)
    return redirect('/myitems')



