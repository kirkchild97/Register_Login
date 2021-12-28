from flask_app.config.mypysqlconnection import connectToMySQL as connect
from flask import flash

class User:
    def __init__(self, data) -> None:
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.date_of_birth = data['date_of_birth']
        self.is_seller = data['is_seller']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    