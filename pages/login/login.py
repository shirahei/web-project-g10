from flask import Blueprint, render_template,request,session,redirect
from utilities.db.customers import Customers

# catalog blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/login')
def index():
    return render_template('login.html')

@login.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@login.route('/login',methods=["POST"])
def login_customer():
    email = request.form.get('email')
    password = request.form.get('password')
    result = Customers.get_customer(email)
    if not result:
        return f"The mail {email} not exists. Try register instead", 400
    elif result[0].password == password:
        session["email"] = result[0].email
        session["fullName"] = result[0].full_name
        session['customer_id']=result[0].customer_id
        session["is_logged_in"] = True
        return redirect('home')
    else:
        return "Incorrect password. Try again.", 400
