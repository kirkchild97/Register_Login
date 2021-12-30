from flask_app import app
from flask import session, request, flash, redirect, render_template, url_for
import flask_app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route('/')
def app_home():
    return render_template('index.html')

@app.route('/try/register', methods=['POST'])
def try_register():
    if User.validate_email(request.form['email']) and User.validate_password(request.form['password'], request.form['repeat_password']):
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password']),
            'date_of_birth' : request.form['dob'],
            'is_seller' : request.form['is_seller']
        }
        User.save_user(data)
        return redirect(url_for('registered'))
    else:
        return redirect('/')

@app.route('/registersuccess')
def registered():
    return render_template('registerSuccess.html')

@app.route('/try/login', methods=['POST'])
def try_login():
    user = User.get_user_data(request.form['email'])
    if bcrypt.check_password_hash(user['password'], request.form['password']):
        data = User.get_user({'id' : user['id']})
        session['first_name'] = data['first_name']
        session['last_name'] = data['last_name']
        session['email'] = data['email']
        session['is_seller'] = data['is_seller']
        session['logged_in'] = True
        return redirect('/loginsuccess')
    else:
        return redirect('/')

@app.route('/loginsuccess')
def logged_in():
    if session['logged_in']:
        return render_template('loginSuccess.html', user = session)
    else:
        return redirect('/')

@app.route('/logout')
def log_out():
    session.clear()
    return redirect('/')