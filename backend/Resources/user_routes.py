from flask import request, jsonify
from flask_restful import Resource
from backend.Services.user_service import UserService
from flask_cors import cross_origin

class UserRegistration(Resource):
    @cross_origin()  # Allow CORS for this route
    def post(self):
        data = request.get_json()
        response, status = UserService.register_user(data)
        print(response)
        return jsonify(response), status

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        response, status = UserService.login_user(data)
        return jsonify(response), status
