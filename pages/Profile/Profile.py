from flask import Blueprint, render_template,session
from utilities.db.customers import Customers

# catalog blueprint definition
Profile = Blueprint('Profile', __name__, static_folder='static', static_url_path='/Profile', template_folder='templates')


# Routes
@Profile.route('/Profile')
def index():
    customer = Customers.get_customer(session.get("email"))

    return render_template('Profile.html',customer_profile = customer[0])
