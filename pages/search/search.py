from flask import Blueprint, render_template

# catalog blueprint definition
search = Blueprint('search', __name__, static_folder='static', static_url_path='/search', template_folder='templates')


# Routes
@search.route('/search')
def index():
    return render_template('search.html')
