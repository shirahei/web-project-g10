from flask import Blueprint, render_template

# homepage blueprint definition
home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')


# Routes
@home.route('/')
@home.route('/home')
def redirect_home():
    return render_template('home.html')
