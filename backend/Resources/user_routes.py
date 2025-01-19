from flask import request, jsonify
from flask_restful import Resource
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserRegistration(Resource):
    def post(self):
        # Get data from the request
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        is_business = data.get("is_business", False)  # Check if user is registering a business
        business_name = data.get("business_name", None)

        from backend.database import User, db, Business
        # Check if user already exists by email
        if User.query.filter_by(email=email).first():
            return {"message": "User already exists"}, 400

        # Check if password is provided
        if not password:
            return {"message": "Password is required"}, 400

        # Check if name is provided
        if not name:
            return {"message": "Name is required"}, 400

        # Hash the password before saving it to the database
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            # Create new user
            new_user = User(name=name, email=email, password_hash=hashed_password, phone=phone)
            db.session.add(new_user)
            db.session.commit()

            # If the user opts to register a business
            if is_business and business_name:
                # Check if business name is provided
                if not business_name:
                    return {"message": "Business name is required when registering as a business"}, 400

                new_business = Business(user_id=new_user.id, name_business=business_name)
                db.session.add(new_business)
                db.session.commit()

            return {"message": "Registration successful!"}, 201

        except Exception as e:
            db.session.rollback()  # Rollback the transaction in case of error
            return {"message": f"Error occurred: {str(e)}"}, 500


# 🚀 User Login Class
class UserLogin(Resource):
    def post(self):
        # Get login data from the request
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")  # User enters plain text password

        from backend.database import User, db, Business
        # Fetch user from the database by email
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"message": "User not found"}, 404

        # Compare entered password with stored hash
        if bcrypt.check_password_hash(user.password_hash, password):
            return {"message": "Login successful!"}, 200
        else:
            return {"message": "Incorrect password"}, 401
