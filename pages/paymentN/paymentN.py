from flask import Blueprint, render_template

# catalog blueprint definition
paymentN = Blueprint('paymentN', __name__, static_folder='static', static_url_path='/paymentN', template_folder='templates')


# Routes
@paymentN.route('/paymentN')
def index():
    return render_template('paymentN.html')
