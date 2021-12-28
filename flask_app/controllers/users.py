from flask_app import app
from flask import session, request, flash, redirect, render_template
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def app_home():
    return render_template('index.html')

@app.route('/try/register', methods=['POST'])
def try_register():
    pass

@app.route('/registersuccess')
def registered():
    return render_template('registerSuccess.html')

@app.route('/try/login', methods=['POST'])
def try_login():
    pass

@app.route('/loginsuccess')
def logged_in():
    pass