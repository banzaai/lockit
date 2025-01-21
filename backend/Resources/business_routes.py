from flask import request, jsonify
from flask_restful import Resource
from backend.Services.business_service import BusinessService

class BusinessRegistration(Resource):
    def post(self):
        data = request.get_json()
        response, status = BusinessService.create_business(data)
        return jsonify(response), status
