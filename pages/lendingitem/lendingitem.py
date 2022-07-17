from flask import Blueprint, render_template

# catalog blueprint definition
lendingitem = Blueprint('lendingitem', __name__, static_folder='static', static_url_path='/lendingitem', template_folder='templates')


# Routes
@lendingitem.route('/lendingitem')
def index():
    return render_template('lendingitem.html')
