from flask import Blueprint, render_template

# catalog blueprint definition
Registration = Blueprint('Registration', __name__, static_folder='static', static_url_path='/Registration', template_folder='templates')


# Routes
@Registration.route('/Registration')
def index():
    return render_template('Registration.html')
