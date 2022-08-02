from flask import Blueprint, render_template,request,redirect
from utilities.db.customers import Customers

# catalog blueprint definition
Registration = Blueprint('Registration', __name__, static_folder='static', static_url_path='/Registration', template_folder='templates')


# Routes
@Registration.route('/Registration')
def index():
    return render_template('Registration.html')

@Registration.route('/Registration',methods=["POST"])
def registration():
    full_name = request.form.get('Fullname')
    email = request.form.get('email')
    neighbourhood = request.form.get('neighbourhood')
    password = request.form.get('password')
    insta_url = request.form.get('insta_url')
    result = Customers.signup_customer(email,password,full_name,neighbourhood,insta_url)
    return redirect('/login')
