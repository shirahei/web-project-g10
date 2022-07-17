from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## home
from pages.home.home import home
app.register_blueprint(home)

## about
from pages.about.about import about
app.register_blueprint(about)

## lendingitem
from pages.lendingitem.lendingitem import lendingitem
app.register_blueprint(lendingitem)

## login
from pages.login.login import login
app.register_blueprint(login)

## paymentN
from pages.paymentN.paymentN import paymentN
app.register_blueprint(paymentN)

## Profile
from pages.Profile.Profile import Profile
app.register_blueprint(Profile)

## Registration
from pages.Registration.Registration import Registration
app.register_blueprint(Registration)

## search
from pages.search.search import search
app.register_blueprint(search)

## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)

###### Components
## Main menu
# from components.main_menu.main_menu import main_menu
# app.register_blueprint(main_menu)
