from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text

from src.db import connect


class Users(Resource):
    def __init__(self):
        self.connection = connect()

    def post(self):
        """create a user """
        data = request.get_json()
        
        fname = data.get('fname', False)

        if not fname:
            return {'error': 'fname is required'}, 400

        query = "INSERT INTO users (fname) VALUES (:fname)"

        try:
            self.connection.execute(sql_text(query), data)
            return "success"
        except:
            return "failed"


    def get(self):
        """ get many users """
        query = "SELECT * from users"
        results = self.connection.execute(query)
        users = results.fetchall()
        return users




class User(Resource):
    def __init__(self):
        self.connection = connect()

    def get(self, user_id):
        """ get info on one user """
        pass

    def put(self, user_id):
        """ update user details """
        pass

    def delete(self, user_id):
        """ delete a user """
        pass
