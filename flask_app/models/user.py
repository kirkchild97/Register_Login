from flask_app.config.mypysqlconnection import connectToMySQL as connect
from flask import flash
import re

class User_Data:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.is_seller = data['is_seller']
        return self

class User:
    def __init__(self, data) -> None:
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.date_of_birth = data['date_of_birth']
        self.is_seller = data['is_seller']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email(email : str) -> bool:
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(email):
            flash("Invalid email address!")
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_password(password : str, check_pass : str) -> bool:
        if password != check_pass: flash('Passwords do not match!')
        return password == check_pass

    @classmethod
    def save_user(cls, data : dict):
        query = '''INSERT INTO users (first_name, last_name, email, password, date_of_birth, is_seller)
        VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(date_of_birth)s, %(is_seller)s)'''
        connect('users').query_db(query, data)
    
    @classmethod
    def get_user_data(cls, email : str) -> User_Data:
        data = { 'email' : email}
        query = '''SELECT id, email, password from users
        WHERE email = %(email)s'''
        results = connect('users').query_db(query, data)
        if results == None:
            flash('Your email or password does not match our records. Please try again')
            return False
        else:
            return results[0]

    @classmethod
    def get_user(cls, data):
        query = '''SELECT first_name, last_name, email, is_seller FROM users
        WHERE id = %(id)s;'''
        results = connect('users').query_db(query, data)
        return results[0]
