from flask import Blueprint, render_template

# catalog blueprint definition
Profile = Blueprint('Profile', __name__, static_folder='static', static_url_path='/Profile', template_folder='templates')


# Routes
@Profile.route('/Profile')
def index():
    return render_template('Profile.html')
