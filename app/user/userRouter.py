from app import api, db
from flask_restx import Resource, Namespace
from app.user.userModel import UserSchema, UserModel
from app.user.userRequest import UserRequest
from flask import request

user_ns = Namespace('users', description="Users Endpoint")


@user_ns.route('/')
class UserAll(Resource):
    @user_ns.doc('user_all')
    def get(self):
        'Returns all users'
        user_schema = UserSchema(many=True)
        query = UserModel.query.all()
        return user_schema.dump(query)


@user_ns.route('/create')
class UserCreate(Resource):
    @user_ns.doc("user_create", body=UserRequest.create())
    def post(self):
        'Creates a user'
        username = request.json["username"]
        password = request.json["password"]
        user = UserModel(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        print(username, password)
        return {
            "message": "Success",
            "data": {
                'username': username
            }
        }, 201


api.add_namespace(user_ns)
