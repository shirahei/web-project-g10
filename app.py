from flask import Flask
from flask import render_template, request, redirect, url_for
from datetime import timedelta
from flask import request, session, jsonify
from flask import session
import time
import requests
import mysql.connector

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('home_func'))


@app.route('/home.html')
def home_func():
    return render_template('home.html')


@app.route('/lendingItem.html')
def lendingItem_func():
    return render_template('lendingItem.html')


@app.route('/login.html')
def login_func():
    return render_template('login.html')


@app.route('/paymentN.html')
def payment_func():
    return render_template('paymentN.html')


@app.route('/Profile.html')
def profile_func():
    return render_template('Profile.html')


@app.route('/Registration.html')
def registration_func():
    return render_template('Registration.html')


@app.route('/search.html')
def search_func():
    return render_template('search.html')


if __name__ == '__main__':
    app.run()
