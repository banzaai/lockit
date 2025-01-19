from flask import request, jsonify
from flask_restful import Resource

# 🚀 Business Registration Class
class BusinessRegistration(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        name_business = data.get("name_business")
        subscription_plan = data.get("subscription_plan", "free")

        from backend.database import User, Business, db
        # Check if business already exists
        if Business.query.filter_by(name_business=name_business).first():
            return {"message": "Business already registered!"}, 400

        # Create new business
        new_business = Business(user_id=user_id, name_business=name_business, subscription_plan=subscription_plan)
        db.session.add(new_business)
        db.session.commit()

        return {"message": "Business registered successfully!"}, 201
